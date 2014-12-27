'use strict';

/**
 * @ngdoc service
 * @name angApp.servicey
 * @description
 * # servicey
 * Service in the angApp.
 */
angular.module('corpus')
.service('movieSearchService', [
        '$http',
        '$q',
        function ($http,$q) {
            console.log('service');
            function searchByTitle(searchTerm){

                return $q(function(resolve,reject){
                    var uriEncodedSearchTerm = encodeURI(searchTerm);
                    $http.get('/movieSearch?searchTerm=' + uriEncodedSearchTerm).
                    success(function(data,status,headers,config){
                        console.log('search method called');
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