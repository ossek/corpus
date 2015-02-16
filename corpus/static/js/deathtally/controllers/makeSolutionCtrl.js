'use strict';
angular.module('corpus')
.controller('makeSolutionCtrl', [
        '$scope',
        'makeSolutionService',
        function ($scope,makeSolutionService) {
            var movieIdUrlPart = /(.*)\/(\d+)\/$/;
            var found = window.location.href.match(movieIdUrlPart);
            var tmdbMovieId = found[2];

            var promise = makeSolutionService.getCreditsForMovie(tmdbMovieId);
            promise.then(
                  function(resultData){
                    $scope.cast = resultData;
                    console.log($scope.cast[0]);
                  },
                  function(err){
                      //todo toast 
                      $scope.getCastError = true;
                      console.log('there has been a problem ' + err);
                  }
                );
        }]);
