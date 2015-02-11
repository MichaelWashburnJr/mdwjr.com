"""
File:		mysite/tracking.py
Language: Python 2 with Django 1.6 Web Framework

Author: Michael D Washburn Jr <mdw7326@rit.edu>

Description: Contains functions to track and log user data.
"""
from models import UserRequest
import IPLookup as ip_lookup

def Log(request):
	if not(request.user.is_superuser):
		page = request.path;
		method = request.method;
		referer = request.META.get('HTTP_REFERER');
		ip = get_client_ip(request);
		ip_info = ip_lookup.GetIPInfo(ip);

		log = UserRequest(
			page=page,
			method=method,
			referer=referer,
			ip=ip,
			city=ip_info["city"],
			state=ip_info["regionName"],
			country=ip_info["country"],
			organization=ip_info["org"]
			);
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