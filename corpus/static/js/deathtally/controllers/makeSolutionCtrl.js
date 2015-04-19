'use strict';
angular.module('corpus')
.controller('makeSolutionCtrl', [
        '$scope',
        '$modal',
        'makeSolutionService',
        '$templateCache',
        '$document',
        function ($scope,$modal,makeSolutionService,$templateCache,$document) {
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
                '<div id="bbq" class="pure-g time-select-modal" >   ' + 
                '  <div class="pure-u-1 pure-u-lg-1-3 characterContainer">   ' + 
                '      <img class="characterImage" src={{castMember.filmImgSrc}} >   ' + 
                '      <p class="characterName">{{castMember.character}}</p>' + 
                '      <p class="actorName">{{castMember.name}}</p>' + 
                '  </div>   ' + 
                '  <div class="pure-u-1 pure-u-lg-2-3 event-select">' + 
                '      <div class="pure-u-1 input-row">' + 
                '          <div class="pure-u-1-5 input-container">' + 
                '              <input id="sliderOutput3" class="event-select-slider" type="text">' + 
                '          </div>' + 
                '      </div>            ' + 
                '      <div class="pure-u-1 slider-row" >   ' + 
                '          <div class="range-slider" data-slider data-options="display_selector: #sliderOutput3; start: 1; end: 344;" >' + 
                '              <span class="range-slider-handle" role="slider" tabindex="0"></span>' + 
                '              <span class="range-slider-active-segment"></span>' + 
                '              <input type="hidden">' + 
                '          </div>' + 
                '      </div>' + 
                '  </div>   ' + 
                ' </div>    ' ;
            $templateCache.put('tpl.html',templateStr);

            $scope.modalDeathTimeSelect = function(castMember){
                jQuery(document).foundation();
                var modalInstance = $modal.open({
                    templateUrl : "tpl.html",
                    controller : 'deathTimeSelectCtrl',
                    resolve : {
                        modalData : function(){
                            return  {castMember : castMember} ;
                        }
                    },
                });

                modalInstance.opened.then(
                        function(somebool){
                            //Do this in this janky way because the 'opened' callback does not wait for the
                            //newly loaded template to be ready, and we need to wait until it's ready 
                            //to init the slider.
                            var elt = $document.find("#bbq"); 
                            elt.ready(function(){
                              jQuery("#bbq").foundation();
                            });
                        });

                modalInstance.result.then(
                        function(modalData){
                            console.log('modal resolved');
                        },
                        function(){
                            console.log('modal dismissed ');
                        });
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
