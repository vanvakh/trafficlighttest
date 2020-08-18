from django.shortcuts import render

from .servises import *
from .models import CustomUser


def posts_view(request):

    if request.method == 'POST':
        if request.POST['action'] == 'delete_data':
            clear_database()
        if request.POST['action'] == 'load_data':
            load_users_data()
            load_posts_data()
    context = {
        'users': get_users(),
        'posts': get_posts()
    }
    return render(request, 'postsapp/index.html', context)