from django.contrib import admin
from django.urls import path
from .views import MovieList , GetMovie

urlpatterns = [
    path('movie-list/', MovieList.as_view() , name='movie-list'),
    path('movie/<str:slug>', GetMovie.as_view() , name='movie')
]