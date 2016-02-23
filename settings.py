"""
Set Config Values for the Mustache build.

Author: Michael Washburn Jr <mdw7326@rit.edu>
"""
import os

# Path to the directory this file is in
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# directory to output the website to
BUILD_DIR = os.path.join(BASE_DIR, 'build')

# directory to search for mustache files in
MUSTACHE_DIR = os.path.join(BASE_DIR, 'mustache')

# directory to copy resources from
RESOURCE_SOURCE_DIR = os.path.join(BASE_DIR, 'resources')
# directory to copy resources to
RESOURCE_BUILD_DIR = os.path.join(BUILD_DIR, 'rsc')
# url to resources directory
RESOURCE_URL = '/rsc'
