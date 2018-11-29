from django.shortcuts import(
    render,
    redirect,
    HttpResponse,
    HttpResponseRedirect,
    get_object_or_404
)
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from . models import Post
from django.contrib import messages
import datetime
from . forms import PostChangeForm, CreatePost
from django.http import JsonResponse
from django.template.loader import render_to_string
import logging
# Create your views here.


def home(request):
    user = request.user

    if user.is_authenticated:
        context = {
            'posts': Post.objects.all(),
            'latest':Post.objects.order_by('-pk')[0],
            'user': user,
        }


        return render(request, 'blog/index.html', context)
    else:
        return redirect('login')

def about(request):
    return render(request, 'blog/about.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        # Redirect to a success page.
            return redirect('homepage')
        else:
            return HttpResponse('Wrong Username or Password')
        # Return an 'invalid login' error message.

        return render(request, 'blog/index.html')
    else:
        form = AuthenticationForm()
        return render(request, 'blog/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def create_new_post(request):
    data = dict()

    if request.method == 'POST':
        form = CreatePost(request.POST)

        if form.is_valid():
            cleaned_title = form.cleaned_data["title"]
            cleaned_content = form.cleaned_data["content"]

            post = Post(title=cleaned_title, content=cleaned_content, author=request.user)
            post.save()

            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = CreatePost()

    context = {'form': form}
    data['html_form'] = render_to_string('blog/edit_post.html',
        context,
        request=request
    )
    return JsonResponse(data)

def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    # post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post
    }

    if request.method == 'POST':
        title = request.POST.get('Name')
        content = request.POST.get('Message')

        post.title = title
        post.content = content
        post.save()
        return render(request, 'blog/index.html' , {'posts': Post.objects.all(),})

    else:
        return render(request, 'blog/update_post.html', context) 