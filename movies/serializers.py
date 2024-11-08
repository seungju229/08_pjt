from rest_framework import serializers
from .models import Genre, Movie

class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class FilterGenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)