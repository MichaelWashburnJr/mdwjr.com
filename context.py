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
                'context' : <page_context>
            }
        }
"""
from settings import RESOURCE_BUILD_DIR

page_map = {
    'home' : {
        'template' : "layout.mustache",
        'path' : "index.html",
        'context' : {
            'RESOURCE_DIR' : RESOURCE_BUILD_DIR,
            'title' : "Michael Washburn Jr",
            'description' : "Michael Washburn's personal website",
            'keywords' : "",
            'css' : [
            ],
            'scripts' : [
            ]
        }
    }
}
