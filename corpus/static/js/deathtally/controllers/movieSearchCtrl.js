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

            $scope.clickSearch = function(){
                console.log('clicked');
                var promise = movieSearchService.searchByTitle($scope.searchTerm);
                promise.then(function(resultData){
                    $scope.searchResults = resultData;
                    $scope.dataAvail = true;
                    console.log('resolved' + resultData[0].filmTitle);
                },function(reason){
                    //todo toast
                    console.log('resolved err' + reason);
                });
            };

        }]);
