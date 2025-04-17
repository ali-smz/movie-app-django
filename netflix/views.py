from netflix.models import Movie
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MovieSerializer

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