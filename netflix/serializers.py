from rest_framework import serializers
from .models import Movie , Like , Comment


class MovieSerializer(serializers.ModelSerializer):
    like_count = serializers.ReadOnlyField()
    comment_count = serializers.ReadOnlyField()
    class Meta:
        model = Movie
        fields = [
            'id', 'title', 'slug', 'description', 'release_date',
            'image', 'duration', 'genre', 'views', 'rating',
            'like_count' , 'comment_count'
        ]


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

class CommentSerializer(serializers.Serializer):
    class Meta:
        model = Comment
        fields = "__all__"