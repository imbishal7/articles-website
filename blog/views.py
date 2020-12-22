from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView)
from .models import Post
from django.utils import timezone


# Create your views here.
def home(request):
    return render(request, 'home.html', context={'insert_me':'Home'})

class AboutView(TemplateView):
    template_name = 'about.html'



class PostListView(ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post
    
