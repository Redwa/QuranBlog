from django.shortcuts import render
from .models import Post
from django.views import generic 
from django.views.generic import TemplateView, ListView, DetailView


# Create your views here.

class PostList(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = 'index.html'

class PostView(DetailView):
  model = Post
  template_name = 'post_detail.html'
  
 
class BlogView(TemplateView):
    template_name = 'blog.html'

class SupplicationsView(TemplateView):
    template_name = 'thamali.html'

class RecitationsView(TemplateView):
    template_name = 'recitations.html'