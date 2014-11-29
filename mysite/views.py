from django.shortcuts import render
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
#def project(request):


"""
A list view of all the projects.
"""
def projects(request):
	projects = Project.objects.all();
	context = {
		'request' : request,
		'projects' : projects
	}
	return render(request, 'Projects/index.html', context);