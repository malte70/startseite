#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# build.py
#     Part of: My homepage on applepie.tardis.mcbx.de
# 
# Copyright (c) 2015 Malte Bublitz, http://malte-bublitz.de
# All rights reserved.
#

import sys
import os
import datetime

try:
	from CLIApp.ansiconsole import ANSIConsole, ANSIColor
	from CLIApp.simple_app import SimpleCLIApp
	
except ImportError:
	print("CLIApp not found!")
	sys.exit(1)
	
class BuildApplication(SimpleCLIApp):
	APP_NAME        = "startseite"
	APP_VERSION      = "0.1"
	fname_style_css  = "www/style.css"
	fname_index_html = "www/index.html"
	
	def version_info(self):
		self.c.writeln(self.APP_NAME + " " + self.APP_VERSION)
		
	def cli_help(self):
		self.version_info()
		self.c.writeln("\nUsage:")
		self.c.writeln("\tbuild.py <options>");
		self.c.writeln("\nOptions:")
		self.c.writeln("\t-V, --version   Show version info")
		self.c.writeln("\t-h, --help      Show this help\n")
		
	def run(self):
		if "--help" in self._options or "-h" in self._options:
			self.version_info()
			
		elif "--version" in self._options or "-V" in self._options:
			self.version_info()
			self.cli_help()
			
		else:
			import config
			
			self.c.writeln("\nRunning build.py for "+self.APP_NAME + " " + self.APP_VERSION + "\n")
			
			self.c.write("Loading templates... ")
			template_css  = open("template.css").read()
			self.c.write("template.css ")
			template_html = open("template.html").read()
			self.c.writeln("template.html")
			
			# CSS
			
			try:
				os.remove(self.fname_style_css)
			except FileNotFoundError:
				pass
				
			self.c.write("Processing CSS template... ")
			css = template_css.replace(
				"%COLOR_BACKGROUND%",
				config.colors["background"]
			).replace(
				"%COLOR_FONT%",
				config.colors["font"]
			).replace(
				"%COLOR_HIGHLIGHT%",
				config.colors["highlight"]
			)
			self.c.writeln("done.")
			
			self.c.writeln("Saving CSS ... done.")
			open(self.fname_style_css, "w").write(css)
			
			# HTML
			
			try:
				os.remove(self.fname_index_html)
			except FileNotFoundError:
				pass
				
			self.c.write("Processing HTML template... ")
			
			#author = os.environ["USER"] + "@" + config.hostname[0]
			author = os.environ["USER"]
			year   = str(datetime.date.today().year)
			
			html = template_html.replace(
				"%TITLE%",
				config.page["title"]
			).replace(
				"%AUTHOR%",
				author
			).replace(
				"%YEAR%",
				year
			).replace(
				"%HEADLINE%",
				config.page["headline"]
			).replace(
				"%FOOTER%",
				config.page["headline"]
                        )
			
			content = ""
			if len(config.links) < 4:
				content += "<ul>\n"
				for l in config.links:
					content += "<li><a href=\"" + l[1] + "\">" + l[0] + "</a></li>\n"
				content += "</ul>\n"
				
			elif len(config.links) == 4:
				content += "<ul>\n"
				for l in config.links[:2]:
					content += "<li><a href=\"" + l[1] + "\">" + l[0] + "</a></li>\n"
				content += "</ul>\n"
				content += "<ul>\n"
				for l in config.links[2:]:
					content += "<li><a href=\"" + l[1] + "\">" + l[0] + "</a></li>\n"
				content += "</ul>\n"
				
			elif len(config.links) > 4:
				for i in range(len(config.links)):
					if i % 3 == 0:
						content += "\t\t\t<ul>\n"
					content += "\t\t\t\t<li><a href=\"" + config.links[i][1] + "\">" + config.links[i][0] + "</a></li>\n"
					if i % 3 == 2:
						content += "\t\t\t</ul>\n"
					#
				
			html = html.replace("%CONTENT%", content)
			self.c.writeln("done.")
			
			self.c.writeln("Saving HTML... done.")
			open(self.fname_index_html, "w").write(html)
			
			self.c.writeln("\nbuild.py done.\n")
	
def main():
	app = BuildApplication()
	app.run()
	
if __name__ == "__main__":
	main()

