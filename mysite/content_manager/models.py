from django.db import models
from .storage import OverwritesStorage
from django.conf import settings
import os

class Page(models.Model):
    """
    The Page model exists only to group Content by pages in order
    to better organize Content in the content management page (not built yet).
    """
    page = models.CharField(max_length=50)

    def __str__(self):
        return self.page

    def get_content(self):
        """
        Return all content objects on this page.
        """
        return Content.objects.filter(page=self)

class Content(models.Model):
    """
    This is a container for one piece of 'content'.
    A piece of 'content' is the simplest form of information normally
    found on the web. It consists of one block of text and a title.
    """
    title = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=30, unique=True)
    body = models.TextField(blank=True,null=True)
    page = models.ForeignKey(Page, related_name='content_set')
    media = models.FileField(storage=OverwritesStorage(), blank=True,null=True)

    def __str__(self):
        return self.name
