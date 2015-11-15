# -*- coding: utf-8 -*-
# 
# config_detect.py
#     Part of: My homepage on applepie.tardis.mcbx.de
# 
# Configuration detection methods for config.py:
# 
# get_local_hostname()
#   -> Get hostname
#   Returns a list containing the hostname and the
#   fully qualified domain name
# 
# get_local_webserver_url(hostname, cafile)
#   hostname => Hostname to use
#               defaults to "localhost"
#   cafile   => Path to CA Certificate file
#               defaults to "~/cacert.pem" if it exists
#   -> Get the URL (i.e. weather to use HTTPS or HTTP)
#      for the local web server
#   Returns the URL
#      HTTPS if available, fall back to HTTP, else returns None
# 
# Copyright (c) 2015 Malte Bublitz, http:/malte-bublitz.de
# All rights reserved.
# 

# os.uname() is used to get the local hostname
from os import uname

import urllib.request

def get_local_hostname():
	return [
		uname().nodename.split(".")[0],
		uname().nodename
	]
	
def get_local_webserver_url(hostname = "localhost", cafile = None):
	url_http  = "http://"  + hostname
	url_https = "https://" + hostname
	
	# Check if local webserver is present
	local_http_response = urllib.request.urlopen(
		url_http
	)
	
	if len(local_http_response.getheader("Server")) < 1:
		return None
		
	if cafile:
		local_https_response = urllib.request.urlopen(
			url_https,
			cafile = cafile
		)
	else:
		local_https_response = urllib.request.urlopen(
			url_https
		)
		
	if len(local_https_response.getheader("Server")) < 1:
		return url_http
		
	else:
		return url_https
		
