from rest_framework import serializers
from movies.models import Keyword, Movie, Genre
from community.models import Review
from django.contrib.auth import get_user_model

class MovieListSerializer(serializers.ModelSerializer):

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
        fields = '__all__'

#####################################################################################

class MovieKeywordRecommandSerializer(serializers.ModelSerializer):

    like_count = serializers.IntegerField(
        source='movie_like_users.count',
        read_only = True
    )
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username')

    class KeywordSerializer(serializers.ModelSerializer):
        class Meta:
            model = Keyword
            fields = ('id', 'word', 'count')

    movie_like_users = UserSerializer(many=True, read_only=True)
    movie_keywords = KeywordSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

###########################################################################################


class MovieSerializer(serializers.ModelSerializer):
    
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name',)


    class ReviewSerializer(serializers.ModelSerializer):

        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('id', 'username')

        user_id = UserSerializer(read_only=True)
        review_like_count = serializers.IntegerField(
            source='like_users.count',
            read_only = True
        )

        class Meta:
            model = Review
            fields = ('id', 'title', 'rank', 'user_id', 'created_at', 'updated_at', 'review_like_count')

    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username')

    class KeywordSerializer(serializers.ModelSerializer):
        class Meta:
            model = Keyword
            fields = ('id', 'word', 'count')
    

    movie_keywords = KeywordSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    movie_to_review = ReviewSerializer(many=True, read_only=True)
    movie_like_users = UserSerializer(many=True, read_only=True)
    like_count = serializers.IntegerField(
        source='movie_like_users.count',
        read_only = True
    )


    class Meta:
        model = Movie
        fields = ('id', 'title', 'movie_keywords', 'movie_like_users', 'like_count', 'poster_path', 'popularity', 'vote_count', 'vote_average', 'overview', 'release_date', 'adult', 'genres', 'movie_to_review')