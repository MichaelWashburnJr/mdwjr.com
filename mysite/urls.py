"""
File:		mysite/urls.py
Language: Python 2 with Django 1.6 Web Framework

Author: Michael D Washburn Jr <mdw7326@rit.edu>

Description: Url definitions for mysite.
"""
from django.conf.urls import patterns, url

from mysite import views

urlpatterns = patterns('',
    url(r'^$', 'mysite.views.index', name='index'),
    url(r'^Resume/$', 'mysite.views.resume', name='resume'),
    url(r'^ContactMe/$', 'mysite.views.contact', name='contact'),
    url(r'^Project/List/$', 'mysite.views.projects', name='projects'),
    url(r'^Project/(?P<project_id>\d+)/info/$', 'mysite.views.project', name='project'),
)