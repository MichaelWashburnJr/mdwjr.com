"""
File:		mysite/tracking.py
Language: Python 2 with Django 1.6 Web Framework

Author: Michael D Washburn Jr <mdw7326@rit.edu>

Description: Contains functions to track and log user data.
"""
from models import UserRequest

def Log(request):
	page = request.path;
	method = request.method;
	referer = request.META.get('HTTP_REFERER');
	ip = get_client_ip(request);

	log = UserRequest(
		page=page,
		method=method,
		referer=referer,
		ip=ip);
	log.save();



###########################################################
# Helpers
###########################################################

"""
Helper function to get a clients IP address.
Source: http://stackoverflow.com/questions/4581789/how-do-i-get-user-ip-address-in-django
"""
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip