import webapp2
import 
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, from the Google App Engine!')

class Welcome(webapp2.RequestHandler):
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
            <p class='section-heading'>Welcome to the Logical Framework Server</p>
            <p class='normal'>This is a prototype demonstrating: 
            <br>1. a service running on the Google App Engine application hosting platform.
            <br>2. routing from a subdomain name to the applicaiton.
            </p>
            </body>
            </html>
        ''')        

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
    ('/', MainPage),
    ('/welcome', Welcome),
    ('/login',Login)
], debug=True)
