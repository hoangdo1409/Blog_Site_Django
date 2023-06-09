from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_created']
    paginate_by = 100

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_created']
    paginate_by = 100

    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_created')

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

def like_post(request, id ):
    post = get_object_or_404(Post, pk=id)
    _id = id
    post.like += 1
    post.save()
    # return render(request, 'blog/post_detail.html')
    return HttpResponseRedirect('/post/1/')

def dislike_post(request, id ):
    post = get_object_or_404(Post, pk=id)
    print(type(id))
    if post.like >= 1:
        post.like -= 1
    elif post.like <= 0:
        post.like -= 0
    post.save()
    # return render(request, 'blog/post_detail.html')
    return HttpResponseRedirect('/post/1/')

def comment_post(request, id):
    post = get_object_or_404(Post, pk=id)

    return HttpResponseRedirect('/post/1/')


def news(request):
    return render(request, 'blog/news.html', {'title': 'News'})