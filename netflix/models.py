from django.db import models
from django.conf import settings


class Movie(models.Model):
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Romance', 'Romance'),
        ('Thriller', 'Thriller'),
        ('Documentary', 'Documentary'),
        ('Animation', 'Animation'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    release_date = models.DateField()
    image = models.URLField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    views = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0)

    @property
    def like_count(self):
        return self.likes.count()
                
    def __str__(self):
        return self.title
    

class Likes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie' , on_delete=models.CASCADE , related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user', 'movie') 
    
    def __str__(self):
        return f"{self.user} liked {self.movie}"
    
