from django.shortcuts import render, get_object_or_404
from content_manager.models import Content

def index(request):
	"""
	The index view. This only has one piece of content.
	"""
	about_me = get_object_or_404(Content, name='about_me')
	my_heading = get_object_or_404(Content, name='my_heading')

	return render(request, 'index.html', {
			'about_me' : about_me,
			'my_heading' : my_heading,
		})

def resume(request):
	"""
	The resume page does not implement the content manager yet.
	"""
	return render(request, 'resume.html')