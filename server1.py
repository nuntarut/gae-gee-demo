#!/usr/bin/env python

import ee
import webapp2
import jinja2
import os

# Authenticate with Earth Engine
EE_ACCOUNT = 'ecodash-beta@appspot.gsericeaccount.com'
EE_PRIVATE_KEY_FILE = 'privatekey.pem'
EE_CREDENTIALS = ee.ServiceAccountCredentials(EE_ACCOUNT, EE_PRIVATE_KEY_FILE)
ee.Initialize(EE_CREDENTIALS)

JINJA2_ENVIRONMENT = jinja2.Environment(
	loader = jinja2.FileSystemLoader(OS.path.dirname(_file_)),
	autoescape = True,
	extensions = ['jinja2.ext.autoescape'])
	
class MainHandler(webapp2.RequestHandler):
	def get(self):
		template_values = {	
			'title': 'Hello from Python!'
		}
		template = JINJA2_ENVIRONMENT.get_template('index.html')
		self.response.out.write(template.render(template_values))

# Setup dynamic routing table
app = webapp2.WSGIApplication([
	('/getmap', GetMapHandler),
	('/', MainHandler)
])



