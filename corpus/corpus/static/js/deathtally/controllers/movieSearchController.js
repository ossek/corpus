'use strict';

/**
 * @ngdoc function
 * @name angApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the angApp
 */
angular.module('corpus')
  .controller('movieSearchCtrl', ['$scope','movieSearchService',function ($scope,movieSearchService) {
      $scope.searchTerm = "";
      $scope.searchResults = [];

      $scope.clickSearch = function(){
          var promise = movieSearchService.searchByTitle($scope.searchTerm);
          promise.then(function(resultData){
              $scope.searchResults = resultData;
          },function(reason){
              //todo toast
              console.log(reason);
          });
      };

  }]);
