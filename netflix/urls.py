from django.urls import path
from .views import MovieList , GetMovie , HotMovies , SuggestedMovies , LikesAPIView , CommentsAPIView

urlpatterns = [
    path('movies/', MovieList.as_view() , name='movies'),
    path('hot-movies/', HotMovies.as_view() , name='hot-movies'),
    path('suggested-movies/', SuggestedMovies.as_view() , name='suggested-movies'),
    path('movie/<str:slug>', GetMovie.as_view() , name='movie'),
    path('movie/<int:movie_id>/like', LikesAPIView.as_view() , name='likes'),
    path('movie/<int:movie_id>/comment', CommentsAPIView.as_view() , name='comments')
]