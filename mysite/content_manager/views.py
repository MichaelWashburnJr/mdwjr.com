from django.shortcuts import render, get_object_or_404
from .decorators import staff_required
from content_manager.models import Content
from .models import *

@staff_required
def create_page(request):
    pass

@staff_required
def create_content(request):
    pass

@staff_required
def edit_page(request, page_id=0):
    pass

@staff_required
def edit_content(request, content_id=0):
    pass

@staff_required
def panel(request):
    """
    Page containing all content objects organized by page.
    """
    pages = Page.objects.all()
    return render(request, "cm_panel.html", {'pages' : pages})

