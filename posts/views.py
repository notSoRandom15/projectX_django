from django.shortcuts import render

from django.views.generic import ListView, CreateView
from .models import Post
from django.urls import reverse_lazy
from .forms import PostForm


class HomePageView(ListView):
    model = Post
    template_name = 'webapp/posts.html'


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'webapp/post.html'
    success_url = reverse_lazy('posts')