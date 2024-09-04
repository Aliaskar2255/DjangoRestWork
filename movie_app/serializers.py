from rest_framework import serializers
from .models import Director, Movie, Review



class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name'. split()
#       fields = 'name'. split()

class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    class Meta:
        model = Movie
        fields = ['title', 'description', 'duration', 'director']

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    class Meta:
        model = Review
        fields = ['text', 'movie']