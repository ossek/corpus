'use strict';
angular.module('corpus')
.controller('makeSolutionCtrl', [
        '$scope',
        '$modal',
        'makeSolutionService',
        '$templateCache',
        function ($scope,$modal,makeSolutionService,$templateCache) {
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
                });

            var templateStr = 
              ' <div class="pure-g" > ' + 
              '     <div class="pure-u-1 pure-u-lg-1-3 characterContainer"> ' + 
              '       <img class="characterImage" src="{{castMember.filmImgSrc}}" > ' + 
              '       <p>{{castMember.character}}</p> ' + 
              '     </div> ' + 
              '     <div class="pure-u-1 pure-u-lg-2-3 timeSelectContainer"> ' + 
              '       <input type="range"> ' + 
              '     </div> ' + 
              ' </div> ';
            $templateCache.put('tpl.html',templateStr);

            $scope.modalDeathTimeSelect = function(castMember){
                var modalInstance = $modal.open({
                    templateUrl : "tpl.html",
                    controller : 'deathTimeSelectCtrl',
                    resolve : {
                        modalData : function(){
                            return  {castMember : castMember} ;
                        }
                    },
                });
                modalInstance.result.then(
                  function(modalData){
                      console.log('modal resolved');
                  },
                  function(){
                      console.log('modal dismissed ');
                  }
                );
            };

            
        }]);

angular.module('corpus')
.controller('deathTimeSelectCtrl', [
        '$scope',
        '$modalInstance',
        'modalData', 
        function($scope,$modalInstance,modalData){

            var resolvedData = 'b';

            $scope.castMember = modalData.castMember;

            $scope.ok = function() {
                $modalInstance.close(resolvedData);
            };

            $scope.cancel = function() {
                $modalInstance.dismiss('cancel');
            };
        }]);
