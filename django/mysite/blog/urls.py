from django.conf.urls import patterns, include, url
import blog.views as views

urlpatterns = patterns('',
    url(r'^$', views.post_list, name='home'),
    url(r'^list$', views.post_list, name='list'),
    url(r'^(?P<slug>[\w-]+)$', views.post_info, name='post'),
    url(r'^projects$', views.project_list, name='project_list')
)