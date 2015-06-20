from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.http import Http404
from blog.models import Post, Tag
from blog.forms import PostForm, TagForm
from django.utils import timezone

###############################################################################
# Display Views
###############################################################################

def project_list(request):
    """
    Display a list of all posts marked as projects.
    """
    #get all posts that are projects and not blog posts
    posts = Post.get_projects()
    context = {
        'posts' : posts,
        'tags' : Tag.get_tags_in_posts(posts).exclude(slug="project"),
        'description' : "This is a list of all my projects",
        'title': "Projects"
    }
    return render(request, 'post_list.html', context)

def post_list(request):
    """
    Display a list of all blog posts (unfiltered)
    """
    posts = Post.get_blog_posts()
    context = {
        'posts' : posts,
        'tags' :  Tag.get_tags_in_posts(posts),
        'description' : "These are all of my blog posts.",
        'title' : "Blog"
    }
    return render(request, 'post_list.html', context)

def post_info(request, slug):
    """
    Displays a blog post in its entirity
    """
    post = get_object_or_404(Post, slug=slug)
    if not post.is_active:
        raise Http404

    #remove the project tag on the info page
    tags = post.tags.exclude(slug='project')
        
    context = {
        'post' : post,
        'tags' : tags
    }
    return render(request, 'post_info.html', context)

###############################################################################
# Form Views
###############################################################################

def create_post(request):
    """
    Form to create a new blog post.
    """
    failure = False
    if request.method == "POST":
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.posted = timezone.now()
            post.save()
        else:
            failure = True
            return render(request, 'post_form.html', {'form' : post_form, 'failure' : True})
    else:
        post_form = PostForm()
    return render(request, 'post_form.html', {
            'form' : post_form,
            'failure' : failure,
            'action' : reverse('blog:create_post')
        })

def edit_post(request, slug):
    """
    Form to edit a blog post.
    """
    failure = False
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        post_form = PostForm(request.POST, instance=post)

        if post_form.is_valid():
            post = post_form.save()
            return redirect('blog:list')
        else:
            failure = True
            return render(request, 'post_form.html', {'form' : post_form, 'failure' : True})
    else:
        post_form = PostForm(instance=post)
    return render(request, 'post_form.html', {
            'form' : post_form,
            'failure' : failure,
            'action' : reverse('blog:edit_post', args=[post.slug])
        })
