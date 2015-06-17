from django.shortcuts import render, redirect
from content_manager.models import Content
from django.contrib import auth
from .utils import get_object_or_none

def login(request):
    """
    Log in the user.
    """
    if request.user.is_authenticated():
        return redirect(request.POST.get('next','index'))
    next = request.POST.get('next')
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect(request.POST.get('next','index'))
        else:
            return render(request, "login.html", {"login_failed": True})

    return render(request, "login.html")

def logout(request):
    """
    Log out the user.
    """
    if request.user.is_authenticated():
        auth.logout(request)
    return redirect("index")

def index(request):
    """
    The index view. This only has one piece of content.
    """
    about_me = get_object_or_none(Content, name='about_me')
    my_heading = get_object_or_none(Content, name='my_heading')

    return render(request, 'index.html', {
            'about_me' : about_me,
            'my_heading' : my_heading,
        })

def resume(request):
    """
    The resume page does not implement the content manager yet.
    """
    resume = get_object_or_none(Content, name='resume')
    return render(request, 'resume.html', {'resume_content' : resume})
    