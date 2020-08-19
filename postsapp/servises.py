import requests
import json

from .forms import CustomUserForm, PostForm
from .models import CustomUser, Post


_USERS_URL = 'http://jsonplaceholder.typicode.com/users'
_POSTS_URL = 'http://jsonplaceholder.typicode.com/posts'

def clear_database():
    CustomUser.objects.all().delete()

def get_posts():
    return (Post.objects.all())

def load_data_to_database():
    """ 
    Loads objects to database. 
    CustomUser first because of ForeignKey Post value.
    """
    user_objects_list = _create_user_objects()
    CustomUser.objects.bulk_create(user_objects_list)
    post_objects_list = _create_post_objects()
    Post.objects.bulk_create(post_objects_list)

def _create_user_objects() -> list:
    """ Creates list of CustomUser objects """
    user_dicts = _parse_users_json()
    user_objects = []
    for user_dict in user_dicts:
        form = CustomUserForm(data=user_dict)
        if form.is_valid():
            user_instance = form.save(commit=False)
            user_objects.append(user_instance)
    return user_objects

def _create_post_objects() -> list:
    """ Creates list of Post objects """
    post_dicts = _parse_posts_json()
    post_objects = []
    for post_dict in post_dicts:
        form = PostForm(data=post_dict)
        if form.is_valid():
            post_instance = form.save(commit=False)
            post_objects.append(post_instance)
    return post_objects

def _parse_users_json() -> list:
    """ Gets users JSON and returns dicts formatted for CustomUserForm """
    users_json = _get_json(_USERS_URL)
    user_dicts = []
    for user in users_json:
        data={
            'id': user.get('id'),
            'name': user.get('name'),
            'username': user.get('username'),
            'email': user.get('email'),
            'address_street': user.get('address').get('street'),
            'address_suite': user.get('address').get('suite'),
            'address_city': user.get('address').get('city'),
            'address_zipcode': user.get('address').get('zipcode'),
            'address_geo_lat': user.get('address').get('geo').get('lat'),
            'address_geo_lng': user.get('address').get('geo').get('lng'),
            'phone': user.get('phone'),
            'website': user.get('website'),
            'company_catchphrase': user.get('company').get('catchPhrase'),
            'company_name': user.get('company').get('name'),
            'company_bs': user.get('company').get('bs')
        }
        user_dicts.append(data)
    return user_dicts

def _parse_posts_json() -> list:
    """ Gets posts JSON and returns dicts formatted for PostForm """
    posts_json = _get_json(_POSTS_URL)
    post_dicts = []
    for post in posts_json:
        data={
            'user_id': post.get('userId'),
            'id': post.get('id'),
            'title': post.get('title'),
            'body': post.get('body'),
        }
        post_dicts.append(data)
    return post_dicts

def _get_json(url: str) -> list:
    """ Makes request to API and returns JSON format data """
    request = requests.get(url)
    return request.json()