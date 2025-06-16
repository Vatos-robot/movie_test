from rest_framework import serializers
from .models import Movie, Actor, Review

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'first_name', 'last_name']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'movie', 'rating', 'description']
        read_only_fields = ['id']

class MovieSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'average_rating']

    def get_average_rating(self, obj):
        return obj.average_rating

class MovieDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = [
            'id', 'title', 'description', 'actors',
            'average_rating', 'reviews'
        ]

    def get_average_rating(self, obj):
        return obj.average_rating
