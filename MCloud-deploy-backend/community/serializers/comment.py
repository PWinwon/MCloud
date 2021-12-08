from rest_framework import serializers
from community.models import Review, Comment
from movies.models import Movie
from django.contrib.auth import get_user_model


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username')
    
    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('id',)

    user_id = UserSerializer(read_only=True)
    review_id = ReviewSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'user_id', 'content', 'review_id')