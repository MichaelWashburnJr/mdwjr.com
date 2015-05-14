from django.shortcuts import render, get_object_or_404, redirect
from .decorators import staff_required
from content_manager.models import Content
from .models import *
from .forms import PageForm, ContentForm

@staff_required
def create_page(request):
    """
    Create a new page.
    """
    if request.method == "POST":
        page_form = PageForm(request.POST)

        if page_form.is_valid():
            page = page_form.save()
            return redirect('cm:panel')

        else:
            return render(request, 'cm_create_page.html', {'page_form' : page_form, 'failure':True})
    page_form = PageForm()
    return render(request, 'cm_create_page.html', {'page_form':page_form})

@staff_required
def edit_page(request, page_id=0):
    """
    Edit an existing page. Also provide the option to delete the page.
    """
    page = get_object_or_404(Page, id=page_id)
    if request.method == "POST":
        page_form = PageForm(request.POST, instance=page)

        if page_form.is_valid():
            if 'submit' in request.POST:
                page_form.save()
            elif 'delete' in request.POST:
                page.delete()
            return redirect('cm:panel')

        else:
            return render(request, 'cm_edit_page.html', {'page_form' : page_form, 'id' : page.id, 'failure':True})
    page_form = PageForm(instance=page)
    return render(request, 'cm_edit_page.html', {'page_form':page_form, 'id' : page.id})

@staff_required
def create_content(request):
    """
    Create a new content object.
    """
    if request.method == "POST":
        content_form = ContentForm(request.POST, request.FILES)

        if content_form.is_valid():
            content = content_form.save()
            return redirect('cm:panel')

        else:
            return render(request, 'cm_create_content.html', {'form' : content_form, 'failure':True})
    content_form = ContentForm()
    return render(request, 'cm_create_content.html', {'form':content_form})

@staff_required
def edit_content(request, content_id=0):
    """
    Edit an existing content object.
    """
    content = get_object_or_404(Content, id=content_id)
    if request.method == "POST":
        content_form = ContentForm(request.POST, request.FILES, instance=content)

        if content_form.is_valid():
            if 'submit' in request.POST:
                content = content_form.save()
            elif 'delete' in request.POST:
                content.delete()
            return render(request, 'cm_edit_content.html', {'form' : content_form, 'id':content.id, 'success':True})
    
        else:
            return render(request, 'cm_edit_content.html', {'form' : content_form, 'id':content.id, 'failure':True})
    content_form = ContentForm(instance=content)
    return render(request, 'cm_edit_content.html', {'form':content_form, 'id':content.id})

@staff_required
def panel(request):
    """
    Page containing all content objects organized by page.
    """
    pages = Page.objects.all()
    return render(request, "cm_panel.html", {'pages' : pages})

