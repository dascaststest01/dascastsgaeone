import os
import sys

import unittest
import webtest

class MainTestCase(unittest.TestCase):
    def test_index(self):
         app = webtest.TestApp(webapp2.WSGIApplication([('/', main.MainHandler),]))
         response = app.get('/')
         self.assertEqual(response.normal_body, 'aaaa')
        
def paths():
    gae_path = './google_appengine'
    
    sys.path.append(gae_path)
    sys.path.append(os.path.join(gae_path, 'google'))
    for dir in ['webob-1.1.1', 'webapp2-2.5.2', 'yaml-3.10']:
        sys.path.append(os.path.join(gae_path, 'lib/{0}'.format(dir)))

if __name__ == '__main__':
    paths()
        
    import webapp2
    import main
    #force build
    unittest.main()
    