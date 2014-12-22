from django.conf.urls import patterns, include, url
from django.contrib import admin
from deathtally.views import apiviews

urlpatterns = patterns('',
        url(r'^$','deathtally.views.views.home_page',name='home'),
        url(r'^films/add$','deathtally.views.views.add_film',name='add_film'),
        url(r'^deathtally/solutions/moviesearch$','deathtally.views.views.moviesearch',name='moviesearch'),
        url(r'^deathtally/solutions/add$','deathtally.views.views.add_deathtally_solution',name='add_deathtally_solution'),
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        url(r'^movieSearch/$', apiviews.movieSearch)
)
