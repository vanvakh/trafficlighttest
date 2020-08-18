from django.forms import ModelForm

from .models import CustomUser, Post


class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'