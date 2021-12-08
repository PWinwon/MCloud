from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from movies.models import Movie
from .serializers import UserInfoSerializer, UserSerializer
from movies.serializers.movie import MovieListSerializer
from accounts import serializers

# Create your views here.

@api_view(['POST'])
def signup(request):
    if request.data.get('password') != request.data.get('password2'):
        return Response({ 'error': '비밀번호가 일치하지 않습니다..ㅠ' }, status.HTTP_400_BAD_REQUEST)
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(['GET'])
def user_profile(request, username):
    User = get_user_model()
    person = get_object_or_404(User, username=username)
    
    # person_like_movies = Movie.objects.filter(movie_like_users=person)
    

    serializer = UserInfoSerializer(person)
    return Response(serializer.data)



