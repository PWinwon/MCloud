from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer


from movies.models import Genre, Keyword, Movie
from movies.serializers.movie import MovieListSerializer, MovieSerializer, MovieKeywordRecommandSerializer
from movies.serializers.recommand import RecommandListSerializer


@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['POST'])
def movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        if movie.movie_like_users.filter(pk=request.user.pk).exists():
            movie.movie_like_users.remove(request.user)
        else:
            movie.movie_like_users.add(request.user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['GET'])
def movie_recommand(request):
    # 유저가 좋아하는 영화의 장르를 뽑아옴
    if request.method == 'GET':
        user_like_movies = Movie.objects.filter(movie_like_users=request.user).values('id', 'genres')
        # serializer = MovieListSerializer(user_like_movies, many=True)
        # return Response(serializer.data)

        # 장르별 카운트 user_dict에 저장
        user_dict = dict()
        for movie in user_like_movies:
            if movie['genres'] in user_dict.keys():
                user_dict[movie['genres']] += 1
            else:
                user_dict[movie['genres']] = 1
        # dict 를 순회하면서 가장 많은 genre와 2번째로 많은 genre 값을 찾는다.
        max_val = -1
        max_genre = 0
        second_val = -1
        second_genre = 0
        for key, val in user_dict.items():
            if max_val < val:
                max_genre = key
                max_val = val
            elif second_val < val:
                second_genre = key
                second_val = val
        # 가장 많은 genre와 2번째 많은 genre에 대해 유저가 좋아요누르지않은 영화를 각각 5개씩
        # 전체 영화에서 유저가 좋아하는 영화 장르의 영화를 뽑으면서 유저가 좋아한 영화는 제외
        genre1 = Genre.objects.get(pk=max_genre)
        genre2 = Genre.objects.get(pk=second_genre)
        recommand_movies1 = Movie.objects.filter(genres=genre1).exclude(movie_like_users=request.user).order_by('-popularity')[:5]
        recommand_movies2 = Movie.objects.filter(genres=genre2).exclude(movie_like_users=request.user).order_by('-popularity')[:5]
        recommand_movies = recommand_movies1|recommand_movies2
        serializer = MovieListSerializer(recommand_movies, many=True)

        return Response(serializer.data)


# 알고리즘 2
# 영화 10개를 무작위로 뽑아서 serializer 로 보내줌
# vue에서는 받아서 각 영화의 키워드 중 랜덤으로 1개를 뽑아서 화면에 보여줌
# 중복체크 후 결과보기를 통해 해당 영화 필터로 추출
@api_view(['GET'])
def movie_recommand_by_keyword(request):
    if request.method == 'GET':
        movies = Movie.objects.exclude(movie_keywords=None)
        serializer = MovieKeywordRecommandSerializer(movies.random(10), many=True)
        return Response(serializer.data)



