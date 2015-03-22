from django.conf.urls import patterns, include, url
import blog.views as views

urlpatterns = patterns('',
	# Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.post_list, name='home'),
    url(r'^post/list$', views.post_list, name='list'),
    url(r'^post/(?P<post_id>\d+)/info$', views.post_info, name='info')
)
