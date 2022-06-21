import imp
from msilib.schema import ListView
from pyexpat import model
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import PostListView
from django.views.generic.edit import PostCreateView
from django.views.generic.edit import PostDetailView
from django.views.generic.edit import PostUpdateView
from django.views.generic.edit import PostDeleteView
from I4G031580IOP.blog.models import Post
from models import blog

# My class views goes here

class blogPostListView(ListView):
    model = Post


# This is postcreateview

class blogCreateView(CreateView):
    models = Post
    fields = "_all_"
    success_url_ = reverse_lazy("blog:all")


# This is Details view class

class blogDetailView(DetailView):
    model = Post


# This is update view class

class blogUpdateView(UpdateView):
    model = Post
    fields = "_all_"
    success_url_ = reverse_lazy("blog:all")


# This is delete view class
class blogDeleteView(UpdateView):
    model = Post
    fields = "_all_"
    success_url_ = reverse_lazy("blog:all")
