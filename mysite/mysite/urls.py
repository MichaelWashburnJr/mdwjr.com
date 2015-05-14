from blog.urls import urlpatterns as blog_urls
from content_manager.urls import urlpatterns as content_manager_urls
from django.conf.urls import patterns, include, url
from django.contrib import admin
import mysite.views as views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^resume$', views.resume, name='resume'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include(blog_urls, namespace='blog')),
    url(r'^contentmanager/', include(content_manager_urls, namespace='content_manager')),
    )
