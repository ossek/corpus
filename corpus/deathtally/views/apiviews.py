from deathtally.apimodels import MovieSearchResult
from deathtally.serializers import MovieSearchResultSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def movieSearch(request):
  #todo query the external tmdb api based on the 'GET' param 'searchTerm'
  result = MovieSearchResult()
  result.filmTitle="Star Wars"
  result.filmImageSrc="https://image.tmdb.org/t/p/original/ghd5zOQnDaDW1mxO7R5fXXpZMu.jpg"
  results = [result]
  serializer = MovieSearchResultSerializer(results,many=True)
  return Response(serializer.data)
