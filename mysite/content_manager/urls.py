from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.urls import urlpatterns as blog_urls
import content_manager.views as views

urlpatterns = patterns('',
    url(r'^panel$', views.panel, name='panel'),
    url(r'^edit/page/(?P<page_id>\d_)$', views.edit_page, name='edit_page'),
    url(r'^edit/content/(?P<content_id>\d_)$', views.edit_content, name='edit_content'),
    url(r'^create/page$', views.create_page, name='create_page'),
    url(r'^create/content$', views.create_content, name='create_content'),
    )
