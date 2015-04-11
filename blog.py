import os
import webapp2
import jinja2
from hello import *
#import re

from google.appengine.ext import db


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                autoescape = True)



class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainPage(Handler):
    def get(self):
        self.write("MainPage!")

class Content(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

class Blog(Handler):
    def render_blog(self):
        blogposts = db.GqlQuery("SELECT * FROM Content ORDER BY created DESC")
        self.render("blog.html", blogposts = blogposts)

    def get(self):
        self.render_blog()


class Newpost(Handler):
    def render_form(self, subject="", content="", error=""):
        self.render("newpost.html", subject=subject, content=content, 
                error=error)

    def get(self):
        self.render_form()

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")

        if subject and content:
            blog_posts = Content(subject = subject, content = content)
            blog_posts.put()
            key_id = blog_posts.key().id()
            print "\nTHIS IS THE ID: ", key_id
            print type(key_id)
            #self.write("Thanks!")
            self.redirect("/blog/"+str(key_id))
        else:
            error = "We need both a subject and content!"
            self.render_form(subject, content, error = error)
        
class Submission(Handler):
    def get(self, product_id):  
        blogpost = Content.get_by_id(int(product_id))
        subject = blogpost.subject
        content = blogpost.content      
        self.render("submission.html", subject=subject, content=content)
    


app = webapp2.WSGIApplication([(r'/', MainPage),
                                (r'/blog', Blog),
                                (r'/blog/(\d+)', Submission),
                                (r'/blog/newpost', Newpost),
                                ('/thanks', Thankshandler),
                                ('/signup', Signup),
                                ('/rot13', Rot13)],
                                debug=True)