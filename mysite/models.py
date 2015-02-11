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
    last_updated = models.DateField('Last Updated');

    def __str__(self):
        return self.title;

    def GetDescriptionPreview(self):
        cutOff = "...";
        maxChars = 160;
        if len(self.description) >  maxChars - len(cutOff):
            return self.description[0:maxChars-len(cutOff)] + cutOff;
        else:
            return self.description;

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
        bad_url = "media/django_project/mysite/"
        url = self.pFile.url.replace(bad_url, "");
        return url;


###############################################################################
# Tracking Models
###############################################################################

"""
A Model representing one request from a user.
"""
class UserRequest(models.Model):
    page = models.CharField(max_length=200);
    method = models.CharField(max_length=10);
    referer = models.CharField(max_length=200, null=True, blank=True);
    ip = models.CharField(max_length=50, null=True, blank=True);
    time = models.DateTimeField(auto_now_add=True);
    #location
    city = models.CharField(max_length=50, null=True, blank=True);
    state = models.CharField(max_length=10, null=True, blank=True);
    country = models.CharField(max_length=100, null=True, blank=True);
    organization = models.CharField(max_length=100, null=True, blank=True);


    def __str__(self):
        return self.ip + ":" + str(self.time);


