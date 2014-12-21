"""
File:       mysite/views.py
Language: Python 2 with Django 1.6 Web Framework

Author: Michael D Washburn Jr <mdw7326@rit.edu>

Description: Views definitions for my personal site.
"""

from django.shortcuts import render, get_object_or_404;
from django.contrib.auth.decorators import login_required;
from django.core.urlresolvers import reverse;
from django.http import HttpResponseRedirect, Http404;
from models import Project, UserRequest;
from forms import ContactForm;
import tracking as t;
from django.db import models;
import datetime;

###############################################################################
# Static Pages
###############################################################################

def index(request):
    t.Log(request);
    return render(request, 'index.html');

def success(request):
    t.Log(request);
    return render(request, 'success.html');
 
def resume(request):
    t.Log(request);
    return render(request, 'Resume/index.html');

def contact(request):
    t.Log(request);
    return render(request, 'ContactMe/index.html');

###############################################################################
# Dynamic Pages
###############################################################################

"""
Sends an email to myself from the user
"""
def send_email(request):
    t.Log(request);
    if request.method == "POST":
        form = ContactForm(request.POST);
        if form.is_valid():
            subject = form.cleaned_data["subject"];
            message = form.cleaned_data["message"];
            sender = form.cleaned_data["sender"];
            form.send_email();
            return HttpResponseRedirect(reverse('mysite:success'));
    else:
        form = ContactForm();
    context = {
        'request' : request,
        'form' : form
    }
    return render(request, 'ContactMe/send_email.html', context)

"""
A view for a single project which displays all project data in an organized
fashion.
"""
def project(request, project_id):
    t.Log(request);
    project = get_object_or_404(Project, pk=project_id);
    links = project.ProjectLinks.all();
    files = project.ProjectFiles.all();
    context = {
        'request' : request,
        'project' : project,
        'links' : links,
        'files' : files
    }
    return render(request, 'Project/info/index.html', context);


"""
A list view of all the projects.
"""
def projects(request):
    t.Log(request);
    projects = Project.objects.all().order_by("-last_updated", "-id")
    context = {
        'request' : request,
        'projects' : projects
    }
    return render(request, 'Project/index.html', context);

###############################################################################
# Admin Pages
###############################################################################

"""
Page for displaying tracking information in a neat manor.
"""
@login_required
def tracking(request):
    if not(request.user.is_superuser):
        raise Http404;
    # Values from Logs #########################################
    total_num_hits = len(UserRequest.objects.all());
    #get the number of unique users
    total_unique_hits = UserRequest.objects.all().values("ip").annotate(n=models.Count("pk"));
    #get unique visits from today
    today = datetime.datetime.now().date();
    today_start = datetime.datetime.combine(today, datetime.time.min);
    todays_unique_hits = UserRequest.objects.filter(time__gte=today_start).values("ip").annotate(n=models.Count("pk"));
    #get hit information per page
    hits_by_page_list = [];
    pages = UserRequest.objects.all().order_by("page").values("page").annotate(n=models.Count("pk"));
    for page in pages:
        page = page["page"];
        #add page path 
        pageList = [page];
        #get all page hits ever
        totalPageHits = UserRequest.objects.filter(page=page);
        pageList.append(len(totalPageHits));
        #get all unique page hits ever 
        pageList.append(len(totalPageHits.values("ip").annotate(n=models.Count("pk"))));
        #get all page hits from today
        todaysPageHits = totalPageHits.filter(time__gte=today_start);
        pageList.append(len(todaysPageHits));
        #get all unique page hits from today
        pageList.append(len(todaysPageHits.values("ip").annotate(n=models.Count("pk"))));

        hits_by_page_list.append(pageList);

    #build list of today's ips with referers and times
    todays_users_list = []
    for ip in todays_unique_hits:
        ip = ip["ip"];
        userHits = UserRequest.objects.filter(ip=ip).order_by("time");
        referer_orig = userHits[0].referer;
        time_orig = userHits[0].time;
        #add this user to the list
        todays_users_list.append([ip,referer_orig, time_orig]);

    #build context and render page
    context = {
        'request' : request,
        'total_num_hits' : total_num_hits,
        'total_num_unique_hits' : len(total_unique_hits),
#        'todays_unique_hits' : todays_unique_hits,
        'hits_by_page_list' : hits_by_page_list,
        'todays_users_list' : todays_users_list,
    }
    return render(request, 'Admin/Tracking/index.html', context);