from django.shortcuts import render, get_object_or_404, redirect

from posts.forms import PostForm
from posts.models import Post
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    return render(request, 'posts/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post-list')
    else:
        form = PostForm()
    return render(request, 'posts/post_edit.html', {'form': form})
