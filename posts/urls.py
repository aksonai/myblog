from django.urls import path
from posts import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]