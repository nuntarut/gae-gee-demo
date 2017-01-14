import ee
import webapp2
import jinja2
import os
import json

EE_ACCOUNT = 'ecodash-beta@appspot.gserviceaccount.com'
EE_PRIVATE_KEY_FILE = 'privatekey.pem'
EE_CREDENTIALS = ee.ServiceAccountCredentials(EE_ACCOUNT, EE_PRIVATE_KEY_FILE)
ee.Initialize(EE_CREDENTIALS)

JINJA2_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    autoescape = True,
    extensions = ['jinja2.ext.autoescape']
)
	
class MainHandler(webapp2.RequestHandler):
    def get(self):
    	template_values={
    	    'title' : 'Hello from Python!',
    	    'M':'I am cat'
    	}
    	template = JINJA2_ENVIRONMENT.get_template('index.html')
    	self.response.out.write(template.render(template_values))
	
class GetMapHandler(webapp2.RequestHandler):
    def get(self):
	
	start_date = '2000-01-01'
	end_date = '2000-12-31'
	
	collection = ee.ImageCollection('MODIS/MYD13A1')
	reference = collection.filterDate(start_date,end_date).sort('system:time_start').select('EVI')
	mymean = ee.Image(reference.mean())
	
	countries = ee.FeatureCollection('ft:1tdSwUL7MVpOauSgRzqVTOwdfy17KDbw-1d9omPw')
	country_names = ['Myanmar (Burma)','Thailand','Laos','Vietnam','Cambodia']
	mekongCountries = countries.filter(ee.Filter.inList('Country', country_names))
		
	fit = mymean.clip(mekongCountries)
	mapid = fit.getMapId({
	    'min': '-400',
	    'max': '400',
	    'bands': ' EVI_mean',
	    'palette' : '931206,ff1b05,fdff42,4bff0f,0fa713'
	})
	
    	map_results = {
    	    'eeMapID': mapid['mapid'],
	    'eeToken': mapid['token']
    	}
   
	self.response.headers['Content-Type'] = 'application/json'
    	self.response.out.write(json.dumps(map_results))

#setup dynamic routing table
app = webapp2.WSGIApplication([
	('/getmap', GetMapHandler),
	('/', MainHandler)
])

