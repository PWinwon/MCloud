from re import L
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from community.serializers.comment import CommentListSerializer, CommentSerializer

from movies.models import Movie


from .models import Comment, Review
from .serializers.review import ReviewListSerializer, ReviewSerializer

# Create your views here.


@api_view(['GET'])
def review_list(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie_id=movie, user_id=request.user)
        return Response(serializer.data)


@api_view(['GET'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def review_update_or_delete(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'PUT':
        serializer = ReviewSerializer(instance=review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie_id=movie)
            return Response(serializer.data)


    if request.method == 'DELETE':
        review.delete()
        return Response(data='delete complete', status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_id=request.user, review_id=review)
            return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    if request.method == 'DELETE':
        comment.delete()
        return Response(data='comment delete complete', status=status.HTTP_204_NO_CONTENT)
    

@api_view(['POST'])
def review_like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)