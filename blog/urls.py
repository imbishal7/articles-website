from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('articles/', views.PostListView.as_view(), name='post_list'),
    path('articles/(?P<pk>\d+)', views.PostDetailView.as_view(), name='post_detail'),
    



]
