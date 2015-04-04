from django.shortcuts import render, get_object_or_404
from blog.models import Post, Tag

def project_list(request):
	"""
	Display a list of all posts marked as projects.
	"""
	context = {
		'posts' : Post.get_projects(),
		'tags' : Tag.objects.exclude(slug="project"),
		'description' : "This is a list of all my projects",
		'title': "Projects"
	}
	return render(request, 'post_list.html', context)

def post_list(request):
	"""
	Display a list of all blog posts (unfiltered)
	"""
	context = {
		'posts' : Post.get_all(),
		'tags' : Tag.objects.all(),
		'description' : "These are all of my blog posts.",
		'title' : "Blog"
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