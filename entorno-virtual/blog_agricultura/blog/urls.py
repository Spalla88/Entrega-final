from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pages/<int:blog_id>/', views.blog_detail, name='blog_detail'),
]