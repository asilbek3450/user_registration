# users/urls.py
from django.urls import path
from .views import register_view, login_view, index

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('', index, name='index'),
]
