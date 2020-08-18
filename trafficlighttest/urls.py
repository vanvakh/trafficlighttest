from django.urls import path, include


urlpatterns = [
    path('posts/', include('postsapp.urls')),
]
