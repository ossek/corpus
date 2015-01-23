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
            $httpBackend.expectGET('/movieSearch?searchTerm=' + uriEncodedSearchTerm + '&page=1')
              .respond(200);
            createController();
            $rootScope.searchTerm = searchTerm;
            $rootScope.clickSearch();
            $httpBackend.flush();
        });
    });

    describe('when search result is not empty',function(){
        it('then correct results are set on scope',function(){
            var searchTerm = 'Anaconda 3';
            var uriEncodedSearchTerm = encodeURI(searchTerm);
            $httpBackend.expectGET('/movieSearch?searchTerm=' + uriEncodedSearchTerm + '&page=1')
              .respond(200,[ {
                      title : 'Anaconda 3', 
                      filmImgSrc : 'http://www.someTmdbUrl.com/someimage_w92.jpg'
                  },
                  {
                      title : 'Anaconda 3 Special Edition', 
                      filmImgSrc : 'http://www.someTmdbUrl.com/someimage2_w92.jpg'
                  }, ]);
            createController();
            $rootScope.searchTerm = searchTerm;
            $rootScope.clickSearch();
            $httpBackend.flush();

            expect($rootScope.searchResults.length).toBe(2);
            expect($rootScope.searchResults[0].filmImgSrc).toBe('http://www.someTmdbUrl.com/someimage_w92.jpg');
            expect($rootScope.searchResults[0].title).toBe('Anaconda 3');
        });
    });

    describe('when search service call gives error',function(){
        it('then error is set on controller',function(){
            var searchTerm = 'Anaconda 3';
            var uriEncodedSearchTerm = encodeURI(searchTerm);
            $httpBackend.expectGET('/movieSearch?searchTerm=' + uriEncodedSearchTerm + '&page=1')
              .respond(500);
            createController();
            $rootScope.searchTerm = searchTerm;
            $rootScope.clickSearch();
            $httpBackend.flush();
            expect($rootScope.searchError).toBe(true);
        });
    });

});
