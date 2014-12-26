from deathtally.apimodels import MovieSearchResult
from deathtally.serializers import MovieSearchResultSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
#import deathtally.service.external.tmdb.movieSearch

@api_view(['GET'])
def movieSearch(request):
  #todo query the external tmdb api based on the 'GET' param 'searchTerm'
  result = MovieSearchResult()
  result.filmTitle="Star Wars"
  result.filmImageSrc="https://image.tmdb.org/t/p/w154/ghd5zOQnDaDW1mxO7R5fXXpZMu.jpg"
  result2 = MovieSearchResult()
  result2.filmTitle="Pride and Prejudice"
  result2.filmImageSrc="https://image.tmdb.org/t/p/w154/AukVKsjZOVR2CBfI3vSJRXNLEKr.jpg"
  results = [result,result2]
  serializer = MovieSearchResultSerializer(results,many=True)
  return Response(serializer.data)
  #print(json.dumps(results))
  #return Response(json.dumps(results))
