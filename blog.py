import os
import webapp2
import jinja2
from hello import *
from validation import valid_username, valid_password, valid_email
#import re

from google.appengine.ext import db


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                autoescape = True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

# def render_post(response, post):
#     response.out.write('<b>' + post.subject + '</b><br>')
#     response.out.write(post.content)


class MainPage(Handler):
    def get(self):
        self.render("hello.html")


class Rot13(Handler):

    def render_rot13(self, text_content = ""):
        self.render("rot13.html", text_content = text_content)
    def get(self):
        self.render_rot13()
    def post(self):
        text = self.request.get("text")
        text_rot13 = self.encode_rot13(text)
        self.render_rot13(text_rot13)

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

# blog
class Content(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)

    # def render(self):
    #     self._render_text = self.content.replace('\n', '<br>')
    #     return render_str("submission.html", p = self)

class Blog(Handler):
    def render_blog(self):
        blogposts = db.GqlQuery("SELECT * FROM Content ORDER BY created DESC limit 10")
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
            self.redirect("/blog/"+str(key_id))
        else:
            error = "We need both a subject and content!"
            self.render_form(subject=subject, content=content, error = error)
        
class Submission(Handler):
    def get(self, product_id):  
        blogpost = Content.get_by_id(int(product_id))
        subject = blogpost.subject
        content = blogpost.content
        date = blogpost.created.strftime("%b %d, %Y")      
        self.render("submission.html", subject=subject, content=content, date=date)

# blog stuff ends here

class Signup(Handler):
    errors = {'email_er' : "",
    'name_er' : "",
    'password_er' : "",
    'verify_pw_er' : ""
    }

    def render_signup(self, username="", email=""):
        self.render("forms_signup.html", username=username, email=email, **errors) 
    
    def get(self):
        self.render_signup() 
        for key in errors:
            errors[key] = ""

    def post(self):
        user_name = self.request.get("username")
        user_pw = self.request.get("password")
        user_verifypw = self.request.get("verify")
        user_email = self.request.get("email")


        flag = True
        if not valid_username(user_name):
            errors['name_er'] = "That's not a valid username."
            flag = False
        if user_email and not valid_email(user_email):
            errors['email_er'] = "That's not a valid email."
            flag = False
        if not valid_password(user_pw):
            errors['password_er'] = "That wasn't a valid password."
            flag = False
        if not user_pw == user_verifypw:
            errors['verify_pw_er'] = "Your passwords didn't match."
            flag = False
        
        if flag:
            self.redirect("/thanks?name=" + user_name)
        else:
            self.render_signup(username=user_name, email=user_email)



class Thankshandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.get("name")
        self.response.out.write("Welcome, {}!".format(name))
    


app = webapp2.WSGIApplication([(r'/', MainPage),
                                (r'/blog', Blog),
                                (r'/blog/(\d+)', Submission),
                                (r'/blog/newpost', Newpost),
                                ('/thanks', Thankshandler),
                                ('/signup', Signup),
                                ('/rot13', Rot13)],
                                debug=True)