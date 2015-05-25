from deathtally.apimodels import MovieSearchResult
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from deathtally.service.external.tmdb.movieSearch import searchByTitle
from deathtally.service.external.tmdb.movieCredits import getCast
from deathtally.service.external.tmdb.movieCredits import getMovieInfo

@api_view(['GET'])
def movieSearch(request):
  searchTerm = request.GET['searchTerm']
  page = request.GET['page']
  results = searchByTitle(searchTerm,page)
  return Response(results,status=status.HTTP_200_OK)

@api_view(['GET'])
def movieCredits(request,tmdbMovieId):
    return Response(getCast(tmdbMovieId),status=status.HTTP_200_OK)

@api_view(['GET'])
def movieInfo(request,tmdbMovieId):
    return Response(getMovieInfo(tmdbMovieId),status=status.HTTP_200_OK)
