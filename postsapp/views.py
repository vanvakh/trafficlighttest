from django.shortcuts import render

from .serviсes import clear_database, get_all_posts, load_data_to_database


def posts_view(request):

    if request.method == 'POST':

        if request.POST['action'] == 'delete_data':
            clear_database()

        if request.POST['action'] == 'load_data':
            load_data_to_database()

    context = {'posts': get_all_posts()}
    return render(request, 'postsapp/index.html', context)
