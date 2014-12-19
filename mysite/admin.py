from django.contrib import admin
from models import Project, ProjectFile, ProjectLink

class ProjectFileInline(admin.StackedInline):
	model = ProjectFile;
	extra = 1;

class ProjectLinkInline(admin.StackedInline):
	model = ProjectLink;
	extra = 1;

class ProjectAdmin(admin.ModelAdmin):
	fields = ['title', 'description', 'last_updated'];
	inlines = [ProjectFileInline, ProjectLinkInline];

admin.site.register(Project, ProjectAdmin);