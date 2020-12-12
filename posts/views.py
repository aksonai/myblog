from django.shortcuts import render
from posts.models import Post


def post_list(request):
    all_posts = Post.objects.all()
    print('test', all_posts)
    return render(request, 'posts/post_list.html', {})
