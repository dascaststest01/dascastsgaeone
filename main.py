import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('its great')
        

routes = [('/', MainHandler),]
app = webapp2.WSGIApplication(routes, debug=True)