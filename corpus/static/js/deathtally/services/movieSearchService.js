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

            function searchByTitle(searchTerm){
                return $q(function(resolve,reject){
                    var uriEncodedSearchTerm = encodeURI(searchTerm);
                    console.log('search term ' + uriEncodedSearchTerm);
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

            function redirectToCreateSolution(tmdbMovieId){
                window.location.href = 'createsolution/' + tmdbMovieId;
            }

            return {
                searchByTitle: searchByTitle,
                redirectToCreateSolution : redirectToCreateSolution,
            };

        }]);
