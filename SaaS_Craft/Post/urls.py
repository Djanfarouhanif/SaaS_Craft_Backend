from django.urls import path
from . import views

urlpatterns = [
    path('api', views.index, name='index'),
    path('api/settings', views.settings, name='settings'),
    path("api/article_post/<str:pk>" , views.article_post, name='article_post'),
    path("api/articleComment/<str:pk>", views.articleComment, name="articleComment"),
    path("api/signup", views.signup, name='signup'),
    path("api/signin", views.signin, name='signin'),
    path('api/logout', views.logout, name='logout')
    
]