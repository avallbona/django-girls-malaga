# -*- encoding: utf-8 -*-

from django.urls import path

from . import views

# urlpatterns = [
#     path('', views.PostList, name='post-list'),
# ]

urlpatterns = [
    path('', views.HomeView.as_view(), name='home-view'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
]
