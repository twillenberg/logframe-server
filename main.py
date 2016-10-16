import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)+"/templates"))

class Welcome(webapp2.RequestHandler):
    def get(self):
        # Define the HTTP headers.
        self.response.headers['Content-Type'] = 'text/html'

        # Obtain the template from the Jinja environment.
        env = JINJA_ENVIRONMENT
        template = env.get_template('default.html')
        app_name = 'Logframe Server'
        date_time = 'Sunday, 16th October 2016'
        url = '/css/default.css'
        output = template.render(app_name=app_name, date_time=date_time, url=url)
        
        # Output the rendered template.
        self.response.write(output)        

class Login(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('''
            <!DOCTYPE html>
            <html>
            <head>
            <link href="/default.css" rel="stylesheet" type="text/css">
            <title>LFS</title>
            </head>
            <body>
            <p class="section-heading">Login</p>
            <p class="normal">Enter your username and password to access the Logframe Server.</p>
            </body>
            </html>
        ''')    
app = webapp2.WSGIApplication([
    ('/', Welcome),
    ('/welcome', Welcome),
    ('/login',Login)
], debug=True)
