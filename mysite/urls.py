from django.conf.urls import patterns, url

from mysite import views

urlpatterns = patterns('',
    url(r'^$', 'mysite.views.index', name='index'),
    url(r'^Resume/', 'mysite.views.resume', name='resume'),
    url(r'^ContactMe/', 'mysite.views.contact', name='contact'),
    url(r'^Projects/', 'mysite.views.projects', name='projects'),
)