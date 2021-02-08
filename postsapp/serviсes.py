import json
from typing import List
from django.db.models.query import QuerySet

import requests

from .forms import CustomUserForm, PostForm
from .models import CustomUser, Post

_USERS_URL = 'http://jsonplaceholder.typicode.com/users'
_POSTS_URL = 'http://jsonplaceholder.typicode.com/posts'


def clear_database() -> None:
    CustomUser.objects.all().delete()


def get_all_posts() -> QuerySet[Post]:
    return Post.objects.all().prefetch_related('user')


def load_data_to_database() -> None:
    """
    Loads objects to database.

    CustomUser first because of ForeignKey Post value.
    """

    users_data = _get_data(_USERS_URL)
    user_objects = _create_user_objects(users_data)
    CustomUser.objects.bulk_create(user_objects)

    posts_data = _get_data(_POSTS_URL)
    post_objects = _create_post_objects(posts_data)
    Post.objects.bulk_create(post_objects)


def _create_user_objects(users: List[dict]) -> List[CustomUser]:
    """Creates list of CustomUser objects."""
    user_objects = []
    for user in users:
        try:
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
                user_objects.append(user_instance)
        except(KeyError):
            print('Invalid JSON structure')
    return user_objects


def _create_post_objects(posts: List[dict]) -> List[Post]:
    """Creates list of Post objects."""
    post_objects = []
    for post in posts:
        try:
            form = PostForm(
                data={
                    'user': post['userId'],
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body']
                }
            )
            if form.is_valid():
                post_instance = form.save(commit=False)
                post_objects.append(post_instance)
        except(KeyError):
            print('Invalid JSON structure')
    return post_objects


def _get_data(url: str) -> List[dict]:
    """Makes request to API and returns list of data dicts."""
    try:
        request = requests.get(url)
        request.raise_for_status()
        return request.json()
    except (requests.RequestException, json.JSONDecodeError) as exc:
        print('Requesting data error: "%s"' % exc)
