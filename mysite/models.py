from django.db import models
from utils import GetUploadSubPath


###############################################################################
# Project Models
###############################################################################


"""
Project Model represents an individual project which has a title,
description, images, links, and supporting files.
"""
class Project(models.Model):
    title = models.CharField(max_length=200);
    description = models.TextField();
    date_posted = models.DateField('Date Posted');

    def __str__(self):
        return self.title;

"""
Link entry for a Project.
"""
class ProjectLink(models.Model):
    project = models.ForeignKey(Project, related_name="ProjectLinks");
    display = models.CharField(max_length=80);
    url = models.CharField(max_length=200);

    def __str__(self):
        return self.display


"""
File entry for a Project.
"""
class ProjectFile(models.Model):
    project = models.ForeignKey(Project, related_name="ProjectFiles");
    display = models.CharField(max_length=80);
    pFile = models.FileField("File",upload_to=GetUploadSubPath);

    def __str__(self):
        return self.display;

    def GetUrl(self):
        bad_url = self.pFile.url;
        url = bad_url[bad_url.find("/media"):];
        return url;
