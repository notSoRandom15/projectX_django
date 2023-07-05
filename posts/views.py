from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView
from .models import Post
from django.urls import reverse_lazy
from .forms import PostForm, UpdateForm




class HomePageView(ListView):
    model = Post
    template_name = 'webapp/posts.html'

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'webapp/post.html'
    success_url = reverse_lazy('posts')

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'webapp/update-file.html'
    success_url = reverse_lazy('posts')