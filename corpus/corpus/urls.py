from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
        url(r'^$','deathtally.views.home_page',name='home'),
        url(r'^films/add$','deathtally.views.add_film',name='add_film'),
        url(r'^deathtally/add$','deathtally.views.add_deathtally_solution',name='add_deathtally_solution')
)
