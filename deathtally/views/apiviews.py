from deathtally.apimodels import MovieSearchResult
from deathtally.serializers import MovieSearchResultSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
#import deathtally.service.external.tmdb.movieSearch
from deathtally.service.external.tmdb.movieSearch import searchByTitle

@api_view(['GET'])
def movieSearch(request):
  #todo query the external tmdb api based on the 'GET' param 'searchTerm'
  results = searchByTitle(request.GET['searchTerm'])
  serializer = MovieSearchResultSerializer(results,many=True)
  return Response(serializer.data)
