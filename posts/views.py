from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView
from .models import Post
from django.urls import reverse_lazy
from .forms import PostForm, UpdateForm
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin



@method_decorator(login_required, name='dispatch')
class HomePageView(ListView):
    model = Post
    template_name = 'webapp/posts.html'

@method_decorator(login_required, name='dispatch')
class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'webapp/post.html'
    success_url = reverse_lazy('posts')

@method_decorator(login_required, name='dispatch')
class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'webapp/update-file.html'
    success_url = reverse_lazy('posts')