# -*- coding: utf-8 -*-
# 
# config.py
#     Part of: My homepage on applepie.tardis.mcbx.de
# 
# Copyright (c) 2015 Malte Bublitz, http:/malte-bublitz.de
# All rights reserved.
# 

# For os.environ and os.path.join
import os

# Helper functions
import config_detect

colors    = {
	"background": "#ecf0f1",
	"font":       "#111111",
	"highlight":  "#2ecc71"
}

page      = {
	"title":    "Startseite",
	"headline": "moin."
}

links     = [
	["Google",      "https://google.com"],
	["Facebook",    "https://facebook.com"],
	["2048",        "../2048/"],
	["addressbook", "../addressbook/"],
	["webdesigns",  "../webdesigns/"]
]

# 
# Add a link to the local webserver if there is one
# Uses HTTPS if possible
# 
try:
	cafile = os.path.join(
		os.environ["HOME"],
		".cacert.pem"
	)
	f = open(cafile)
	f.read(1)
	f.close()
	
except FileNotFoundError:
	cafile = None
	
hostname  = config_detect.get_local_hostname()
local_url = config_detect.get_local_webserver_url(hostname[1], cafile)

if local_url:
	links.append([hostname[0], local_url])
	
