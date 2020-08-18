from django.shortcuts import render

from .servises import *
from .models import CustomUser


def posts_view(request):
    context = {

    }
    return render(request, 'postsapp/index.html', context)