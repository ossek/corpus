from deathtally.apimodels import MovieSearchResult
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from deathtally.service.external.tmdb.movieSearch import searchByTitle
from deathtally.service.external.tmdb.movieCredits import getCast

@api_view(['GET'])
def movieSearch(request):
  results = searchByTitle(request.GET['searchTerm'])
  return Response([r.__dict__ for r in results],status=status.HTTP_200_OK)

@api_view(['GET'])
def movieCredits(request,tmdbMovieId):
    return getCast(tmdbMovieId)
