import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('aaaaa')
        

routes = [('/', MainHandler),]
app = webapp2.WSGIApplication(routes, debug=True)