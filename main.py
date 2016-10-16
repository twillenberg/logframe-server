import webapp2
from jinja2 import Template

env = Environment(loader=PackageLoader('webtester', 'templates'))

class Welcome(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = env.get_template('default.html')

        template = Template("""""")
        self.response.write(template.render(app_name="Logical Framework Server"))        

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
