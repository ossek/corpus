'use strict';

/**
 * @ngdoc service
 * @name angApp.servicey
 * @description
 * # servicey
 * Service in the angApp.
 */
angular.module('corpus')
  .service('movieSearchService', ['$http','$q',function ($http,$q) {
    // AngularJS will instantiate a singleton by calling "new" on this function

      function searchByTitle(searchTerm){

          return $q(function(resolve,reject){
              var uriEncodedSearchTerm = encodeURI(searchTerm);
              $http.get('/deathtally/movieSearch?searchTerm=' + uriEncodedSearchTerm).
              success(function(data,status,headers,config){
                  resolve(data);
                }).
              error(function(data,status,headers,config){
                  reject(data);
              });
              
          });
      }

      return {
          searchByTitle: searchByTitle
      };
    
  }]);
