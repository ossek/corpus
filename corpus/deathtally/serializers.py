from deathtally.apimodels import MovieSearchResult
from rest_framework import serializers

class MovieSearchResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MovieSearchResult
        fields = ('filmTitle','filmImageSrc')
