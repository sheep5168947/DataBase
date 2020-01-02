from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Search/', views.Search, name='Search'),
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
    path('profile/', views.profile, name='profile'),
    path('editPost/', views.editPost, name='editPost'),
    path('aggressive_mobs/', views.aggressive_mobs, name='aggressive_mobs'),
    path('neutral_mobs/', views.neutral_mobs, name='neutral_mobs'),
    path('Overworld/', views.Overworld, name='Overworld'),
    path('Nether/', views.Nether, name='Nether'),
    path('End/', views.End, name='End'),
    path('tools/', views.tools, name='tools'),
    path('foods/', views.foods, name='foods'),
    path('ores/', views.ores, name='ores'),
    #path('biomes/', views.biomes, name='biomes'),
    path('biome/', views.biome, name='biome'),
    path('structures/', views.structures, name='structures'),
    path('building_materials/',views.building_materials,name='building_materials'),
    path('backtomain/',views.backtomain,name='backtomain'),
    path('Steve/',views.Steve,name='Steve')
]