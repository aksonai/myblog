from django.urls import path
from posts import views

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('posts/<int:pk>', views.post_detail, name='post-detail'),
    path('post/new/', views.post_new, name='post_new'),
]