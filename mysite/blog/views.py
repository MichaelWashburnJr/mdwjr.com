from django.shortcuts import render, get_object_or_404
from django.http import Http404
from blog.models import Post, Tag

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
    print(slug)
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