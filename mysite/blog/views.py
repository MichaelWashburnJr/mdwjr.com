from blog.forms import PostForm, TagForm
from blog.models import Post, Tag
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
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

@login_required
def edit_tags(request):
    """
    Form to create a new blog tag.
    """
    if not request.user.is_staff:
        raise Http404

    tags = list(Tag.get_all())
    edit_forms = []
    if request.method == "GET":
        edit_forms = [TagForm(prefix=tag.id, instance=tag) for tag in tags]
        add_form = TagForm()
    elif request.method == "POST":
        #Process the Forms
        if "delete-tag" in request.POST:
            tag = get_object_or_404(Tag,id=request.POST["delete-tag"])
            tag.delete()
            return redirect('blog:edit_tags')
            
        #Add tag if necessary
        if "add-tag" in request.POST:
            add_form = TagForm(request.POST)
            if add_form.is_valid():
                add_form.save()
                return redirect('blog:edit_tags')
        else:
            add_form = TagForm()

        #Save edits
        if "save-tags" in request.POST:
            edit_forms = [TagForm(request.POST, prefix=tag.id, instance=Tag()) for tag in tags]
            #Save all te edit forms
            for i in range(len(tags)):
                if edit_forms[i].is_valid():
                    tag = edit_forms[i].save(commit=False)
                    tags[i].name = tag.name
                    tags[i].slug = tag.slug
                    tags[i].save()
        else:
            edit_forms = [TagForm(prefix=tag.id, instance=tag) for tag in tags]

    return render(request, 'tag_form.html', {
        'edit_forms' : edit_forms,
        'add_form'   : add_form,
        })

@login_required
def create_post(request):
    """
    Form to create a new blog post.
    """
    if not request.user.is_staff:
        raise Http404
        
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

@login_required
def edit_post(request, slug):
    """
    Form to edit a blog post.
    """
    if not request.user.is_staff:
        raise Http404
        
    failure = False
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        post_form = PostForm(request.POST, instance=post)

        if post_form.is_valid():
            post = post_form.save()
            return redirect('blog:post', post.slug)
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
