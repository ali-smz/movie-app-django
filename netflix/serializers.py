from rest_framework import serializers
from .models import Movie , Likes


class MovieSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = [
            'id', 'title', 'slug', 'description', 'release_date',
            'image', 'duration', 'genre', 'views', 'rating',
            'like_count'
        ]

    def get_like_count(self , obj):
        return obj.likes.count()

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = "__all__"
