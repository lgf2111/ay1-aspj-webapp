
<h1 align="center">
  <br>
  <a href="https://flask-blog.lgf2111.repl.co/"><img src="./misc_src/Icon.png" alt="Flask Blog" width="200"></a>
  <br>
  Flask Blog Secure
  <br>
</h1>

<h4 align="center">A blog hosting website using <a href="https://flask.palletsprojects.com/" target="_blank">Flask</a>, with main focus on making it secure.</h4>
<br>
<p align="center">
  OWASP Top 10 (2017) Covered:<br>
  <a href="https://owasp.org/www-project-top-ten/2017/A1_2017-Injection">A1:2017-Injection
  </a></br>
  <a href="https://owasp.org/www-project-top-ten/2017/A2_2017-Broken_Authentication">A2:2017-Broken Authentication
  </a></br>
  <a href="https://owasp.org/www-project-top-ten/2017/A3_2017-Sensitive_Data_Exposure">A3:2017-Sensitive Data Exposure
  </a><br>
  <a href="https://owasp.org/www-project-top-ten/2017/A5_2017-Broken_Access_Control">A5:2017-Broken Access Control
  </a></br>
  <a href="https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration">A6:2017-Security Misconfiguration
  </a></br>
  <a href="https://owasp.org/www-project-top-ten/2017/A7_2017-Cross-Site_Scripting_(XSS)">A7:2017-Cross-Site Scripting (XSS)
  </a></br>
  <a href="https://owasp.org/www-project-top-ten/2017/A8_2017-Insecure_Deserialization">A8:2017-Insecure Deserialization
  </a></br>
  <a href="https://owasp.org/www-project-top-ten/2017/A10_2017-Insufficient_Logging%2526Monitoring">A10:2017-Insufficient Logging & Monitoring
  </a>
<br>
<br>
</p>
<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#contributors">Contributors</a> •
  <a href="#credits">Credits</a> •
  <a href="#related">Related</a>
</p>

![screenshot](./misc_src/Website%20Screenshot.png)

## Key Features

* Login Authentication
  - Registration
  - Login
    - Remember Me
    - Forget Password
  - Account
    - C.R.U.D User
    - 2 Factor Authorization
* Home Page
  - Display all posts
    - Pagination
  - Able to comment on posts
  - Able to purchase premium plan
    - Free Plan - Limited to 1 post/day
    - Premium Plan - No limitations
* C.R.U.D Post
  - Create new post
  - Read individual posts
  - Update own post
  - Delete own post
* Admin Page
  - Only admin can access this page
  - Able to modify all models
    - User, Post, Comment, Role
  - Dashboard page
    - See traffic within this web application


## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/) (which comes with [pip](https://pypi.org/project/pip/)) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/lgf2111/flask-blog-secure

# Go into the repository
$ cd flask-blog-secure

# Install dependencies
$ pip install -r requirements.txt

# Run the app 
# (Make sure have enrivonment variables ready)
$ python run.py
```

There are [scripts](.//db_scripts/) for you to use to manipulate the database with ease:

```bash
# Create/Recreate database
# (Make sure have enrivonment variables ready)
$ python db_scripts/create_db.py

# Make specific user admin (Eg: lgf2111)
$ python db_scripts/make_admin.py
$ Username: lgf2111

# Reset login attempt for specific user (Eg: lgf2111)
$ python db_scripts/reset_login_attempt.py
$ Username: lgf2111
```

> **Note**
> 
> If `pip` doesn't work, try `pip3`. 
> 
> If `python` doesn't work, try `python3`.
>


> **Warning**
> 
> This web application uses environmental variables. You will need to have them before running the it:
> - [EMAIL_USER]()
> - [EMAIL_PASS](https://support.google.com/accounts/answer/185833?hl=en)
> - [SECRET_KEY](https://stackoverflow.com/questions/34902378/where-do-i-get-a-secret-key-for-flask)
> - [SQLALCHEMY_DATABASE_URI](https://stackoverflow.com/questions/43466927/sqlalchemy-database-uri-not-set)
> - [STRIPE_PUBLISHABLE_KEY](https://stripe.com/docs/keys)
> - [STRIPE_SECRET_KEY](https://stripe.com/docs/keys)
> - [SENTRY_SDK_DSN](https://docs.sentry.io/product/sentry-basics/dsn-explainer/)


## Contributors

This web application will not be possibly done without this team of developers:

- [Justin](https://www.instagram.com/sun.w.k/) (Project Leader)
  - [A3:2017-Sensitive Data Exposure](https://owasp.org/www-project-top-ten/2017/A3_2017-Sensitive_Data_Exposure)
  - [A8:2017-Insecure Deserialization](https://owasp.org/www-project-top-ten/2017/A8_2017-Insecure_Deserialization)
- [Ivan](https://www.instagram.com/_ivan_teo_/) (Timekeeper)
  - [A1:2017-Injection](https://owasp.org/www-project-top-ten/2017/A1_2017-Injection)
  - [A2:2017-Broken Authentication](https://owasp.org/www-project-top-ten/2017/A2_2017-Broken_Authentication)
- [Chee Hao](https://www.instagram.com/cheeh0w/) (Lead Developer)
  - [A5:2017-Broken Access Control](https://owasp.org/www-project-top-ten/2017/A5_2017-Broken_Access_Control)
  - [A7:2017-Cross-Site Scripting (XSS)](https://owasp.org/www-project-top-ten/2017/A7_2017-Cross-Site_Scripting_(XSS))
- [Guan Feng](https://www.instagram.com/lgf2111/) (Scrum Master)
  - [A6:2017-Security Misconfiguration](https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration)
  - [A10:2017-Insufficient Logging & Monitoring](https://owasp.org/www-project-top-ten/2017/A10_2017-Insufficient_Logging%2526Monitoring)

## Credits

This application uses the following open source packages:

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-Admin](https://pypi.org/project/Flask-Admin/)
- [Flask-Bcrypt](https://pypi.org/project/Flask-Bcrypt/)
- [flask_csp](https://pypi.org/project/flask-csp/)
- [Flask_Limiter](https://pypi.org/project/Flask_Limiter/)
- [Flask_Login](https://pypi.org/project/Flask_Login/)
- [Flask_Mail](https://pypi.org/project/Flask_Mail/)
- [Flask_MonitoringDashboard](https://pypi.org/project/Flask_MonitoringDashboard/)
- [Flask_SQLAlchemy](https://pypi.org/project/Flask_SQLAlchemy/)
- [Flask_WTF](https://pypi.org/project/Flask_WTF/)
- [itsdangerous](https://pypi.org/project/itsdangerous/)
- [Pillow](https://pypi.org/project/Pillow/)
- [pycryptodome](https://pypi.org/project/pycryptodome/)
- [sentry_sdk](https://pypi.org/project/sentry_sdk/)
- [stripe](https://pypi.org/project/stripe/)
- [WTForms](https://pypi.org/project/WTForms/)


## Related

[Flask_Blog](https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog) - CoreyMSchafer

## Support

<a href="https://www.buymeacoffee.com/lgf2111" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

<p>Or</p> 

<a href="https://www.patreon.com/lgf2111">
	<img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>


****