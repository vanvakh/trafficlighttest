from django.shortcuts import render
from .servises import *


def posts_view(request):
    json_list = []
    if request.method == 'POST':
        json_list = get_json()
    context = {
        "json": json_list
    }
    return render(request, 'postsapp/index.html', context)