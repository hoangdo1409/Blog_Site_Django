from django.urls import path
from users_blog import views

urlpatterns = [
    path('', views.register, name='register'),
]