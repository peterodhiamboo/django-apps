from django import forms
from django.contrib.auth.models import User
from blog.models import Post
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User

        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )

class PostChangeForm(ModelForm):

    class Meta:
         model = Post
         fields = ('title','content')
