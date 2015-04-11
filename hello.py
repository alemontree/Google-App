import webapp2
import cgi
import re
import jinja2
from validation import valid_username, valid_password, valid_email


# form = """
#     <form method= "post" action="">
#     <textarea name="text"
#     style="height: 100px; width: 400px;">{}</textarea>
#     <input type= "submit">
#     </form>
#     """

form_signup = """
    <h1><b>Signup</b></h1>
    <form method= "post" action= "">
        <table>
            <tr>
                <td align="right">Username: </td>
                <td align="left"><input input type="text" name="username"
                value="{username}"/></td>
                <td style="color:red">{name_er}</td>
            </tr>
            <tr>
                <td align="right">Password: </td>
                <td align="left"><input type ="password" name="password"/></td>
                <td style="color:red">{password_er}</td>
            </tr>
            <tr>
                <td align="right">Verify Password: </td>
                <td align="left"><input type="password"
                name="verify"/></td>
                <td style="color:red">{verify_pw_er}</td>
            </tr>
            <tr>
                <td align="right">Email(optional): </td>
                <td align="left"><input type="text" name="email"
                value="{email}"/></td>
                <td style="color:red">{email_er}</td>
            </tr>
        </table>
        <br>
        <input type= "submit"/>
    </form>
    """
errors = {'email_er' : "",
    'name_er' : "",
    'password_er' : "",
    'verify_pw_er' : ""
}

# class MainPage(Handler):
#     def render_main(self):
#         self.render("hello.html")

#     def get(self):
#         self.render_main()

        # intro = """
        # <body bgcolor="paleturquoise">
        # <font size="6"
        # <h2><b>Welcome to Mikhail's Google App Practice Website!</b></h2><br>
        # <br>
        # Please check out my apps:
        # <br>
        # <a href="/rot13">Rot13 Encoder</a><br>
        # <a href="/signup">Signup</a><br>
        # <br>

        # <div style="color:brown">Have a nice day!</div>
        # </font>
        # </body>

        # """
        #self.response.headers['Content-Type'] = 'text/plain'
        # self.response.out.write(intro)

    # def post(self):
    #     text = self.request.get('text')
    #     sef.response.out.write(text)

# class Rot13(webapp2.RequestHandler):


#     def write_form(self, content=""):
#         self.response.out.write(form.format(content))
#     def get(self):
#         self.write_form()
#     def post(self):
#         text = self.request.get("text")
#         text = self.escape_html(text)
#         text_rot13 = self.encode_rot13(text)
#         self.write_form(text_rot13)
#         print text_rot13

#     def encode_rot13(self, s):
#         esc_str_flag = 0
#         res = []
#         for c in s:
#             if c == "&" and esc_str_flag == 0:
#                 esc_str_flag = 1                
#             if esc_str_flag == 1 and c == ";":
#                 esc_str_flag = 0                
#             if esc_str_flag == 0:
#                 res.append(c.encode('rot13'))
#             else:
#                 res.append(c)
#         return "".join(res)

#     def escape_html(self, s):
#         return cgi.escape(s, quote = True)

# class Signup(webapp2.RequestHandler):

#     def write_form(self, username="", email=""):
#         self.response.out.write(form_signup.format(username=username,
#                                                     email=email, **errors))
    
#     def get(self):
#         self.write_form() 

#     def post(self):
#         user_name = self.escape_html(self.request.get("username"))
#         user_pw = self.escape_html(self.request.get("password"))
#         user_verifypw = self.escape_html(self.request.get("verify"))
#         user_email = self.escape_html(self.request.get("email"))

#         flag = True
#         if not valid_username(user_name):
#             errors['name_er'] = "That's not a valid username."
#             flag = False
#         if user_email and not valid_email(user_email):
#             errors['email_er'] = "That's not a valid email."
#             flag = False
#         if not valid_password(user_pw):
#             errors['password_er'] = "That wasn't a valid password."
#             flag = False
#         if not user_pw == user_verifypw:
#             errors['verify_pw_er'] = "Your passwords didn't match."
#             flag = False

        
#         if flag:
#             self.redirect("/thanks?name=" + user_name)
#         else:
#             self.write_form(username=user_name, email=user_email)


#     def escape_html(self, s):
#         return cgi.escape(s, quote = True)

# class Thankshandler(webapp2.RequestHandler):
#     def get(self):
#         name = self.request.get("name")
#         self.response.out.write("Welcome, {}!".format(name))


       

# application = webapp2.WSGIApplication(['/thanks', Thankshandler)],
#                                          debug=True)