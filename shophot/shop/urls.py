from django.urls import path, include

from . import views

#app_name='search'
urlpatterns = [
    path('feed/', views.feed),
    path('post/', views.post),
    path('home/', views.home)
  	

]