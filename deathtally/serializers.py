from deathtally.apimodels import MovieSearchResult
from rest_framework import serializers

#can make the api browsable. see http://www.django-rest-framework.org/topics/browsable-api/
class MovieSearchResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MovieSearchResult
        fields = ('filmTitle','filmImageSrc')
