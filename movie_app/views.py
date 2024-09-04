from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer



@api_view(['GET'])
def director_list_api_view(request):
    directors = Director.objects.all()
    data = DirectorSerializer(directors, many=True).data
    return Response(data=data)

@api_view(['GET'])
def director_detail_api_view(request, id):
    director = Director.objects.get(id=id)
    data = DirectorSerializer(director, many=False).data
    return Response(data=data)


@api_view(['GET'])
def movie_list_api_view(request):
    movies = Movie.objects.all()
    data = MovieSerializer(movies, many=True).data
    return Response(data=data)

@api_view(['GET'])
def movie_detail_api_view(request, id):
    director = Movie.objects.get(id=id)
    data = MovieSerializer(director, many=False).data
    return Response(data=data)



@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(reviews, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_detail_api_view(request, id):
    director = Review.objects.get(id=id)
    data = ReviewSerializer(director, many=False).data
    return Response(data=data)