"""
File:		mysite/IPLookup.py
Language: Python 2

Author: Michael D Washburn Jr <mdw7326@rit.edu>

Description: Grabs IP address information from an external API
and returns a python dictionary containing the xml elements and
their values.
"""
from urllib2 import urlopen
import xml.etree.ElementTree as ET

API_URL = "http://ip-api.com/xml/"

"""
Returns an XML ElementTree when given an IP address to lookup.
The XML tree contains information for the IP.
The XML Contains the following elements:
	status, country, countryCode, region, regionName, city,
	zip, lat, lon, timezone, isp, org, as, query
"""
def GetXMLFromAPI(ip_address):
	#get the xml code from the api for the ip address
	print(API_URL + ip_address);
	content = urlopen(API_URL + ip_address).read()
	#parse the xml and get the root element
	return ET.fromstring(content)

"""
Converts the XML ElementTree object into a python dictionary.
"""
def XMLToDict(xml):
	info = {}
	#for each element in the xml
	for child in xml:
		info[child.tag] = child.text
	return info

"""
Returns a dictionary of IP address information for the given
IP address.
"""
def GetIPInfo(ip_address):
	return XMLToDict(GetXMLFromAPI(ip_address))
