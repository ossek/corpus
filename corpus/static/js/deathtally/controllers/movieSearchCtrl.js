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
            $scope.searchResultPages = [];
            $scope.dataAvail = false;
            $scope.searchError = false;

            $scope.clickSearch = function(){
                $scope.searchError = false;
                $scope.searchResultPages = [];
                $scope.dataAvail = false;
                searchByTitleAndPage($scope.searchTerm,1);
            };

            function searchByTitleAndPage(searchTerm,page){
                var promise = movieSearchService.searchByTitle($scope.searchTerm,page);
                promise.then(function(resultData){
                    $scope.searchResultPages.push({
                        nextClicked : false, 
                        resultData : resultData,
                        nextResultPage : function(){
                            this.nextClicked = true;
                            searchByTitleAndPage(searchTerm,page+1);
                        }
                    });
                    $scope.dataAvail = true;
                },function(reason){
                    //todo toast
                    $scope.searchError = true;
                    console.log('resolved err' + reason);
                });
            }

            $scope.movieSelectAction = function(tmdbMovieId){
                movieSearchService.redirectToCreateSolution(tmdbMovieId);
            };

        }]);
