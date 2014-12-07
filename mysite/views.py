"""
File:		mysite/views.py
Language: Python 2 with Django 1.6 Web Framework

Author: Michael D Washburn Jr <mdw7326@rit.edu>

Description: Views definitions for my personal site.
"""

from django.shortcuts import render, get_object_or_404
from models import Project

###############################################################################
# Static Pages
###############################################################################

def index(request):
    return render(request, 'index.html')
 
def resume(request):
    return render(request, 'Resume/index.html')

def contact(request):
	return render(request, 'ContactMe/index.html')

###############################################################################
# Dynamic Pages
###############################################################################

"""
A view for a single project which displays all project data in an organized
fashion.
"""
def project(request, project_id):
	project = get_object_or_404(Project, pk=project_id);
	links = project.ProjectLinks.all();
	files = project.ProjectFiles.all();
	context = {
		'request' : request,
		'project' : project,
		'links' : links,
		'files' : files
	}
	return render(request, 'Project/info/index.html', context);


"""
A list view of all the projects.
"""
def projects(request):
	projects = Project.objects.all().order_by("-date_posted", "-id").reverse();
	context = {
		'request' : request,
		'projects' : projects
	}
	return render(request, 'Project/index.html', context);