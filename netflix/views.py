from .models import Movie , Likes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MovieSerializer , LikeSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

class MovieList(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data , status=200)


class GetMovie(APIView):
    def get(self, request, slug):
            movie = Movie.objects.get(slug=slug)
            serializer = MovieSerializer(movie)
            return Response(serializer.data , status=200)
    
class HotMovies(APIView):
     def get(self, request):
          movies = Movie.objects.all().order_by('-views')[:5]
          serializer = MovieSerializer(movies, many=True)
          return Response(serializer.data , status=200)

class SuggestedMovies(APIView):
     def get(self, request):
          movies = Movie.objects.order_by('?')[:10]
          serializer = MovieSerializer(movies, many=True)
          return Response(serializer.data , status=200)
     
class LikesAPIView(APIView):
     permission_classes = [IsAuthenticated]

     def post(self , request , movie_id) :
          movie = get_object_or_404(Movie , id = movie_id)
          like , created = Likes.objects.get_or_create(user = request.user , movie=movie)

          if not created:
               return Response({"detail": "You have already liked this movie."}, status=status.HTTP_400_BAD_REQUEST)

          serializer = LikeSerializer(like)
          return Response(serializer.data , status=status.HTTP_201_CREATED)