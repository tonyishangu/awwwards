from .models import Project,UserProfile
from django.contrib.auth.models import User
from .models import UserProfile,Project
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms

class NewProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('project_title','project_description','landing_page','live_site')


class VoteForm(ModelForm):
    class Meta:
        model = Project
        fields = ('design','usability','content')


class ProfileEditForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic','bio')

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')