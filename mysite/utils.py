"""
File: mysite/utils.py
Description: Contains helper functions for other parts of the code.
"""

#####################################################################
# Model helpers
#####################################################################

"""
Returns a sub path to the upload_to function of the FileField Model
field.
"""
def GetUploadSubPath(instance, filename):
	return ("django_project/mysite/media/" + instance.project.title + '/' + filename)

