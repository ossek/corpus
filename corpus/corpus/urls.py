from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
        url(r'^$','deathtally.views.home_page',name='home'),
        url(r'^films/new$','deathtally.views.new_film',name='new_film')
)
