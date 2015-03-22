from django.shortcuts import render, get_object_or_404
from blog.models import Post

def post_list(request):
	"""
	Display a list of all blog posts (unfiltered)
	"""
	context = {
		'posts' : Post.objects.all(),
	}
	return render(request, 'post_list.html', context)

def post_info(request, post_id=0):
	"""
	Displays a blog post in its entirity
	"""
	post = get_object_or_404(Post, pk=post_id)
	context = {
		'post' : post,
	}
	return render(request, 'post_info.html', context)