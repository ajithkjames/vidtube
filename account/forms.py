from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from account.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = "__all__"

class CustomUserCreationForm(UserCreationForm):

	def __init__(self, *args, **kwargs):
		super(CustomUserCreationForm, self).__init__(*args, **kwargs)

		for fieldname in ['username', 'password1', 'password2']:
		    self.fields[fieldname].help_text = None

	class Meta:
	    model = get_user_model()
	    fields = ("username",)

	def clean_username(self):
	    username = self.cleaned_data["username"]
	    try:
	        get_user_model().objects.get(username=username)
	    except get_user_model().DoesNotExist:
	        return username
	    raise forms.ValidationError(self.error_messages['duplicate_username'])