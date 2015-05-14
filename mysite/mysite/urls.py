from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.urls import urlpatterns as blog_urls
import mysite.views as views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^resume$', views.resume, name='resume'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include(blog_urls, namespace='blog')),
    )
