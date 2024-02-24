from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path("article_post/<str:pk>" , views.article_post, name='article_post'),
    path("articleComment/<str:pk>", views.articleComment, name="articleComment"),
    
]