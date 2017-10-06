from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from account.models import User
from core.models import Video


class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ['title','description','category','file','thumbnail']
