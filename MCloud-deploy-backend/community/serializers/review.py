from rest_framework import serializers
from community.models import Review, Comment
from movies.models import Movie
from django.contrib.auth import get_user_model


class ReviewListSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title')
    

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username')
    
    user_id = UserSerializer(read_only=True)
    movie_id = MovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title')

    
    class CommentSerializer(serializers.ModelSerializer):
        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('id', 'username')

        user_id = UserSerializer(read_only=True)

        class Meta:
            model = Comment
            fields = ('id', 'content', 'review_id', 'user_id')


    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username')

    user_id = UserSerializer(read_only=True)
    movie_id = MovieSerializer(read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    like_users = UserSerializer(many=True, read_only=True)
    like_count = serializers.IntegerField(
        source='like_users.count',
        read_only = True
    )


    class Meta:
        model = Review
        fields = ('id', 'user_id', 'movie_id', 'like_users', 'title', 'rank', 'content', 'created_at', 'updated_at', 'comment_set', 'like_count')