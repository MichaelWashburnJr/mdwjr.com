from django.contrib import admin
from models import Project, ProjectFile, ProjectLink, UserRequest

class ProjectFileInline(admin.StackedInline):
	model = ProjectFile;
	extra = 1;

class ProjectLinkInline(admin.StackedInline):
	model = ProjectLink;
	extra = 1;

class ProjectAdmin(admin.ModelAdmin):
	fields = ['title', 'description', 'last_updated'];
	inlines = [ProjectFileInline, ProjectLinkInline];

class UserRequestAdmin(admin.ModelAdmin):
	fields = ['page', 'method', 'referer', 'ip']

admin.site.register(Project, ProjectAdmin);
admin.site.register(UserRequest, UserRequestAdmin);