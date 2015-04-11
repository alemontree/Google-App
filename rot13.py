import webapp2
import cgi


def escape_html(s):
    return cgi.escape(s, quote = True)

form = """
<form method= "post" action="/rot13">
    <textarea name="text"></textarea>
</form>
"""


class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(form)

    def post(self):
        text = self.request.get('text')
        sef.response.out.write(text)

        

#class Testhandler(webapp2.RequestHandler):
#    def post(self):
#        q = self.request.get("q")
#        self.response.out.write(q)
#
#        self.response.headers['Content-Type'] = 'text/plain'
#        self.response.out.write(self.request)


        

application = webapp2.WSGIApplication([('/', MainPage)],
                                         debug=True)