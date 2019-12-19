from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Search/<str:search_name>/', views.Search, name='Search'),
    path('reply_login/', views.reply_login, name='reply_login'),
    path('reply_post/', views.reply_post, name='reply_post'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('main/<str:username>/', views.main, name='main'),
    path('producer/', views.producer, name='producer'),
    path('post/<str:username>/', views.post, name='post'),
    path('ALLpost/', views.ALLpost, name='ALLpost'),
    path('getPost/', views.getPost, name='getPost'),
    path('deletePost/', views.deletePost, name='deletePost'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('editPost/', views.editPost, name='editPost'),
    
]