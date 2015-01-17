'use strict';

/**
 * @ngdoc function
 * @name angApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the angApp
 */
angular.module('corpus')
.controller('movieSearchCtrl', [
        '$scope',
        'movieSearchService',
        function ($scope,movieSearchService) {

            $scope.searchTerm = "";
            $scope.searchResults = [];
            $scope.dataAvail = false;
            $scope.searchError = false;

            $scope.clickSearch = function(){
                $scope.searchError = false;
                var promise = movieSearchService.searchByTitle($scope.searchTerm);
                promise.then(function(resultData){
                    $scope.searchResults = resultData;
                    $scope.dataAvail = true;
                },function(reason){
                    //todo toast
                    $scope.searchError = true;
                    console.log('resolved err' + reason);
                });
            };
            
            $scope.movieSelectAction = function(tmdbMovieId){
                movieSearchService.redirectToCreateSolution(tmdbMovieId);
            };

        }]);
