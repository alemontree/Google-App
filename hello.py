import webapp2
import cgi


form = """
<form method= "post" action="">
    <textarea name="text"
    style="height: 100px; width: 400px;">{}</textarea>
    <input type= "submit">
</form>
"""


class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write("Hello to Mikhail's Google App Website!")

    def post(self):
        text = self.request.get('text')
        sef.response.out.write(text)

class Rot13(webapp2.RequestHandler):
    def write_form(self, content=""):
        self.response.out.write(form.format(content))
    def get(self):
        self.write_form()
    def post(self):
        text = self.request.get("text")
        text = self.escape_html(text)
        text_rot13 = self.encode_rot13(text)
        self.write_form(text_rot13)
        print text_rot13

    def encode_rot13(self, s):
        esc_str_flag = 0
        res = []
        for c in s:
            if c == "&" and esc_str_flag == 0:
                esc_str_flag = 1                
            if esc_str_flag == 1 and c == ";":
                esc_str_flag = 0                
            if esc_str_flag == 0:
                res.append(c.encode('rot13'))
            else:
                res.append(c)
        return "".join(res)


    def escape_html(self, s):
        return cgi.escape(s, quote = True)


#class Testhandler(webapp2.RequestHandler):
#    def post(self):
#        q = self.request.get("q")
#        self.response.out.write(q)
#
#        self.response.headers['Content-Type'] = 'text/plain'
#        self.response.out.write(self.request)


        

application = webapp2.WSGIApplication([('/', MainPage),
                                        ('/rot13', Rot13)],
                                         debug=True)