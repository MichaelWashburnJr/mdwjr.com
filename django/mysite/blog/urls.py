from django.conf.urls import patterns, include, url
import blog.views as views

urlpatterns = patterns('',
	# Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.post_list, name='home'),
    url(r'^Post/List/', views.post_list, name='list'),
    url(r'^Post/(?P<post_id>\d+)/Info/', views.post_info, name='info'),
    url(r'^Projects/', views.project_list, name='project_list')
)