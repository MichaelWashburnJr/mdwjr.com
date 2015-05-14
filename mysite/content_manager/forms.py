from django import forms
from .models import *

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['page']


class ContentForm(forms.ModelForm):

    class Meta:
        model = Content
        fields = ['title', 'name', 'page','media', 'body']
