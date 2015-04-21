from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.urls import urlpatterns as blog_urls

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog', include(blog_urls, namespace="blog")),
    )
