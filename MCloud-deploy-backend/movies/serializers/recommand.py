from rest_framework import serializers
from movies.models import Movie, Genre
from django.contrib.auth import get_user_model


class RecommandListSerializer(serializers.ModelSerializer):
    
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
        fileds = '__all__'

