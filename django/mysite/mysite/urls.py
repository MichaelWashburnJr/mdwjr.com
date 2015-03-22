from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.urls import urlpatterns as blog_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^d/admin/', include(admin.site.urls)),
    url(r'^d/Blog/', include(blog_urls, namespace="blog")),
    )
