import requests, json


USERS_URL = 'http://jsonplaceholder.typicode.com/users'
POSTS_URL = 'http://jsonplaceholder.typicode.com/posts'

def get_json():
    request = requests.get(USERS_URL)
    return(request.json())

