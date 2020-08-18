import requests, json
from django.db import DatabaseError, transaction

from .forms import CustomUserForm, PostForm
from .models import CustomUser, Post


USERS_URL = 'http://jsonplaceholder.typicode.com/users'
POSTS_URL = 'http://jsonplaceholder.typicode.com/posts'

def clear_database():
    CustomUser.objects.all().delete()

def get_posts():
    return (Post.objects.all())

def load_users_data():
    users_json = get_json(USERS_URL)
    users_list = []
    for user in users_json:
        form = CustomUserForm(
            data={
                    'id': user['id'],
                    'name': user['name'],
                    'username': user['username'],
                    'email': user['email'],
                    'address_street': user['address']['street'],
                    'address_suite': user['address']['suite'],
                    'address_city': user['address']['city'],
                    'address_zipcode': user['address']['zipcode'],
                    'address_geo_lat': user['address']['geo']['lat'],
                    'address_geo_lng': user['address']['geo']['lng'],
                    'phone': user['phone'],
                    'website': user['website'],
                    'company_catchphrase': user['company']['catchPhrase'],
                    'company_name': user['company']['name'],
                    'company_bs': user['company']['bs']
            }
        )
        if form.is_valid():
            user_instance = form.save(commit=False)
            users_list.append(user_instance)
    CustomUser.objects.bulk_create(users_list)

def load_posts_data():
    posts_json = get_json(POSTS_URL)
    posts_list = []
    for post in posts_json:
        form = PostForm(
            data={
                    'user_id': post['userId'],
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body'],
            }
        )
        if form.is_valid():
            post_instance = form.save(commit=False)
            posts_list.append(post_instance)
    Post.objects.bulk_create(posts_list)

def get_json(url):
    request = requests.get(url)
    return request.json()