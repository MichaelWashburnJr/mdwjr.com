"""
Add all pages to be rendered as keys page_map with the given values.

Author: Michael Washburn Jr <mdw7326@rit.edu>

Example:
The following example shows how to define a page in the page_map.

    Variable Descriptions:
        - page_name: the name of the page to build. This does not have to correspond to any other
          value
        - template_filee: the mustache template to use to build the page
        - page_context: the context dictionary to pass into the renderer when building the page

    Structure:
        page_map = {
            <page> : {
                'template' : <tempplate_file>,
                'path' : <path_to_output>
                'context' : {
                    <page> : True,
                    ...
                }
            }
        }
"""
from settings import RESOURCE_URL, MUSTACHE_DIR
import os

page_map = {
    'home' : {
        'template' : "layout.mustache",
        'path' : "index.html",
        'context' : {
            'home' : True,
            'RESOURCE_DIR' : RESOURCE_URL,
            'title' : "Michael Washburn Jr",
            'description' : "Michael Washburn's personal website",
            'keywords' : "",
            'css' : [
                {'file' : RESOURCE_URL + "/custom/css/home.css"}
            ],
            'scripts' : [
                {'file' : RESOURCE_URL + "/custom/js/home.js"}
            ]
        }
    },
    'resume' : {
        'template' : "layout.mustache",
        'path' : os.path.join("resume","index.html"),
        'context' : {
            'resume' : True,
            'RESOURCE_DIR' : RESOURCE_URL,
            'title' : "My Resume",
            'description' : "Michael Washburn's Resume",
            'keywords' : "resume",
            'css' : [
                {'file' : RESOURCE_URL + "/custom/css/resume.css"}
            ],
            'scripts' : [
            ]
        }
    },
    'error' : {
        'template' : "layout.mustache",
        'path' : os.path.join("error","index.html"),
        'context' : {
            'error' : True,
            'RESOURCE_DIR' : RESOURCE_URL,
            'title' : "Error",
            'description' : "",
            'keywords' : "",
            'css' : [
            ],
            'scripts' : [
            ]
        }
    }
}

blog_list_context = {
    'blog_list' : True,
    'RESOURCE_DIR' : RESOURCE_URL,
    'title' : "Blog",
    'description' : "Michael Washburn's Blog",
    'keywords' : "blog",
    'posts' : [],
    'css' : [
        {'file' : RESOURCE_URL + "/custom/css/blog_list.css"}
    ],
}

blog_map = {
    'blog_django-server-setup' : {
        'template' : "layout.mustache",
        'path' : os.path.join("blog","django-server-setup","index.html"),
        'url' : "/blog/django-server-setup/",
        'content_file' : os.path.join(MUSTACHE_DIR, "blog_posts", "django-server-setup.html"),
        'context' : {
            'blog_post' : True,
            'RESOURCE_DIR' : RESOURCE_URL,
            'title' : "Django Server Setup",
            'description' : "A tutorial for setting up a Django server on Ubuntu using NGINX, \
                             PostgreSQL, and Gunicorn.",
            'keywords' : "turorial, django, nginx, postgres, ubuntu, linux ",
            'date' : "April 7, 2015",
            'content' : "",
            'css' : [
                {'file' : RESOURCE_URL + "/custom/css/blog_posts.css"}
            ],
            'scripts' : [
            ]
        }
    }
}
