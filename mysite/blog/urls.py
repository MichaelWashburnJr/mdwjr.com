from django.conf.urls import patterns, include, url
import blog.views as views

urlpatterns = patterns('',
    url(r'^$', views.post_list, name='home'),
    url(r'^list$', views.post_list, name='list'),
    url(r'^projects$', views.project_list, name='project_list'),
    url(r'^(?P<slug>[\w-]+)$', views.post_info, name='post'),
    url(r'^create/post$', views.create_post, name='create_post'),
    url(r'^edit/tags', views.edit_tags, name='edit_tags'),
    url(r'^edit/(?P<slug>[\w-]+)$', views.edit_post, name='edit_post'),
)