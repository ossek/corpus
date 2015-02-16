'use strict';
angular.module('corpus')
.service('makeSolutionService', [
        '$http',
        '$q',
        function ($http,$q) {

            function getCreditsForMovie(tmdbMovieId){
                return $q(function(resolve,reject){
                  $http.get('/movie/' + tmdbMovieId + '/credits').
                    success(function(data,status,headers,config){
                        resolve(data);
                    }).
                    error(function(data,status,headers,config){
                        reject(data);
                    });
                 });
            }

            return {
                getCreditsForMovie : getCreditsForMovie,
            };
        }]);
