from django.shortcuts import render

from .servises import *


def posts_view(request):
    if request.method == 'POST':
        if request.POST['action'] == 'delete_data':
            clear_database()
        if request.POST['action'] == 'load_data':
            load_data_to_database()
    posts = get_posts()
    context = {
        'posts': posts
    }
    return render(request, 'postsapp/index.html', context)