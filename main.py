import webapp2

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
            <p class='normal'>On this server you can securely manage and report againts a logical framework.</p>
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
