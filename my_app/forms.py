from django import forms
from my_app.models import Post,Comment,User_info
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta():
        model=Post
        fields=('title','text')

        widgets = {
            'title': forms.Textarea(attrs={
                'class': 'editable medium-editor-textarea postcontent form-control',
                'rows': '2'
                }),
            'text': forms.Textarea(attrs={
                'class': 'editable medium-editor-textarea postcontent form-control',
                'rows': '4'
                }),
        }


class CommentForm(forms.ModelForm):
    class Meta():
        model=Comment
        exclude=('post','author','create_date')

        widgets = {
    
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }


class UserForm(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'text-center'}))
    class Meta():
        model=User
        fields=('username','password','email')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model=User_info
        fields=('profilepic','type_of_user','facebook')
