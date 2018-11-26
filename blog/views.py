from django.shortcuts import(
    render,
    redirect,
    HttpResponse,
    HttpResponseRedirect
)
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from . models import Post
from django.contrib.auth import logout
from django.contrib import messages
import datetime
# Create your views here.


def home(request):
    user = request.user

    if user.is_authenticated:
        context = {
            'posts': Post.objects.all(),
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

def createPost(request):
    heading = request.POST['title']
    message = request.POST['message']

    if len(heading) == 0 or len(message) == 0:
        return render('<h1> That cant be left Empty !! </h1>')
    else:
        post = Post(title=heading, content=message, author=request.user)
        post.save()
        messages.success(request, '%s your post has been created !' % request.user.username)
    return redirect('homepage')
