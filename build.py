"""
Build the Mustache Website located in this directory into the "build" directory.

Author: Michael Washburn Jr <mdw7326@rit.edu>
Notes:
    - All mustache files should be located in the ./mustache/ directory
    - All resources such as CSS, JavaScript, Images, etc. should be located in the
      RESOURCE_SOURCE_DIR directory.
"""
import os
import pystache
import shutil
import time

#local imports
from settings import *
from context import page_map, blog_list_context, blog_map

def make_dirs():
    """Create any directories needed to build if they do not exist already"""
    # make a list of all directories needed. Note: RESOURCE_BUILD_DIR is done seperately
    directories = [BUILD_DIR, os.path.join(BUILD_DIR, "blog")]
    # get each directory that pages will be built to
    for page in page_map.keys():
        path = os.path.dirname(os.path.join(BUILD_DIR,page_map[page]['path']))
        if path not in directories:
            directories.append(path)
    # get each directory blogs will be built to
    for blog in blog_map.keys():
        path = os.path.dirname(os.path.join(BUILD_DIR,blog_map[blog]['path']))
        if path not in directories:
            directories.append(path)
    # make each path if it does not exist
    for directory in directories:
        if not os.path.exists(directory):
            os.mkdir(directory)

def copy_resources():
    """
    Copy resources folder to build directory
    Source: http://pythoncentral.io/how-to-recursively-copy-a-directory-folder-in-python/
    """
    try:
        shutil.copytree(RESOURCE_SOURCE_DIR, RESOURCE_BUILD_DIR)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

def clean(retry=True):
    """Cleans the build directory"""
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)

def build_pages():
    """Build each page defined in the page_map and the blog posts defined in blog_map"""
    # Change to mustache directory for rendering
    os.chdir(MUSTACHE_DIR)
    r = pystache.Renderer()
    # Build each regular page
    for page in page_map.keys():
        # grab values from the page_map
        template = os.path.join(MUSTACHE_DIR, page_map[page]['template'])
        path = os.path.join(BUILD_DIR, page_map[page]['path'])# full path to the output file
        context = page_map[page]['context']
        # render the page
        output = r.render_path(template, context)
        # save the output to the file
        f = open(path, "w")
        f.write(output.replace("\r\n", "\n"))
        f.close()
    # Build each blog post, and the Blog List
    for blog in blog_map.keys():
        template = os.path.join(MUSTACHE_DIR, blog_map[blog]['template'])
        path = os.path.join(BUILD_DIR, blog_map[blog]['path'])
        context = blog_map[blog]['context']
        # Read the contents of the blog
        f = open(blog_map[blog]['content_file'])
        content = f.read()
        f.close()
        #Render and write the file
        context['content'] = content
        output = r.render_path(template, context)
        f = open(path, "w")
        f.write(output.replace("\r\n", "\n"))
        f.close()
        blog_list_context['posts'].append(blog_map[blog])
    # Render the blog list
    output = r.render_path(os.path.join(MUSTACHE_DIR,"layout.mustache"), blog_list_context)
    f = open(os.path.join(BUILD_DIR, "blog", "index.html"), "w")
    f.write(output.replace("\r\n", "\n"))
    f.close()
    # Change back to the base dir
    os.chdir(BASE_DIR)

def main():
    clean()
    make_dirs()
    copy_resources()
    build_pages()

if __name__ == '__main__':
    main()
