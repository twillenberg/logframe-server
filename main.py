import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="templates"))

class Welcome(webapp2.RequestHandler):
    def get(self):
        # Define the Http headers.
        self.response.headers['Content-Type'] = 'text/html'

        # Obtain the template from the Jinja environment.
        env = JINJA_ENVIRONMENT
        template = env.get_template('default.html')
        app_name = "Logical Framework Server"
        date_time = "Today"
        output = template.render(app_name="Logical Framework Server", date_time=date_time)
        
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
