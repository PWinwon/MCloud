from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.models import Review

from movies.models import Movie

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username',]


class UserInfoSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        like_count = serializers.IntegerField(
            source='movie_like_users.count',
            read_only = True
        )

        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('id', 'username')

        movie_like_users = UserSerializer(many=True, read_only=True)

        class Meta:
            model = Movie
            fields = ('id', 'title', 'overview', 'like_count', 'movie_like_users', 'poster_path' )
    

    class ReviewSerializer(serializers.ModelSerializer):
        class MovieSerializer(serializers.ModelSerializer):
            like_count = serializers.IntegerField(
                source='movie_like_users.count',
                read_only = True
            )

            class UserSerializer(serializers.ModelSerializer):
                class Meta:
                    model = get_user_model()
                    fields = ('id', 'username')

            movie_like_users = UserSerializer(many=True, read_only=True)
            class Meta:
                model = Movie
                fields = ('id', 'title', 'overview', 'like_count', 'movie_like_users', 'poster_path' )

        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('id', 'username')

        user_id = UserSerializer(read_only=True)
        movie_id = MovieSerializer(read_only=True)

        class Meta:
            model = Review
            fields = '__all__'
    
    user_like_movies = MovieSerializer(many=True, read_only=True)
    user_to_review = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'user_like_movies', 'user_to_review')