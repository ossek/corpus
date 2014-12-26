'use strict';
//when enter key is used to search, search is done
//done in ui

describe('movie search tests',function(){
    beforeEach(module('corpus'));

    var $httpBackend,$rootScope,$controller,$scope,movieSearchService,createController;

    beforeEach(inject(function($injector) {
        $rootScope = $injector.get('$rootScope');
        $controller = $injector.get('$controller');
        $httpBackend = $injector.get('$httpBackend');
        movieSearchService = $injector.get('movieSearchService');

        createController = function(){
            return $controller('movieSearchCtrl',{
                '$scope' : $rootScope,
                'movieSearchService' : movieSearchService
            });
        };

    }));

    afterEach(function(){
        $httpBackend.verifyNoOutstandingExpectation();
        $httpBackend.verifyNoOutstandingRequest();
    });
        

    describe('when search is clicked ',function(){

        it('service is called',function(){ 
            var searchTerm = 'Anaconda 3';
            var uriEncodedSearchTerm = encodeURI(searchTerm);
            $httpBackend.expectGET('/deathtally/movieSearch?searchTerm=' + uriEncodedSearchTerm)
              .respond(200);
            createController();
            $rootScope.searchTerm = searchTerm;
            $rootScope.clickSearch();
            $httpBackend.flush();
        });

    });

});
