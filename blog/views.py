# -*- encoding: utf-8 -*-

# Create your views here.
from django.views.generic import ListView, DetailView

from blog.models import Post


class HomeView(ListView):
    queryset = Post.objects.all()
    template_name = 'blog/home.html'


class PostDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = 'blog/post.html'
