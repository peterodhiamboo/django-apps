from django import forms
import blog.models as models


class CreatePost(forms.ModelForm):

    title = forms.CharField( widget=forms.Textarea(attrs={"placeholder":"Title", "rows":1, "cols":45}), max_length=150)
    content = forms.CharField( widget=forms.Textarea(attrs={"placeholder":"Content", "rows":6, "cols":45}), max_length=500)

    class Meta:
        model = models.Post
        fields = ['title', 'content']




class PostChangeForm(forms.ModelForm):

    class Meta:
         model = models.Post
         fields = ['title','content']