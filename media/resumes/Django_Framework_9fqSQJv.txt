Django Framework
--------------------------------------
Requirement to learn django
	a) html
	b) css
	c) bootstrap
	d) javascript
	e) python

- django perform 90% work. The remaining 10% you have to perform.
- Django is the framework for developing web application using python.
- It is based on MVT(Model View and Template) design pattern.
- what is mean by MVT
	M --> model(database)
	V --> bussiness logic
	T --> Template(the area on which the actual data displayed)

- The django is very demanding due to its rapid development feature.
- It takes less time to build application after collecting the client requirement.
- By using django we can build web application in very less time, django is desgined in such a manner that it
  handles much of configure things automatically.

Other application mvc pattern (model, view, controller)
model --> database
view --> the area in which we can get actual data.(html pages--> frontend)
controller --> bussiness logic


What is the histroy of django?
-------------------------------------
- Django was initially developed by Adrian Holovaty and Simon Willison, while working at the Lawrence Journal newspaper in kansas, USA in the year of 2003.

- The goal was to build a framework that could handle the fast paced content updates required for news paper.
- The framework focused reusability, scalability and avoiding repetitive code.
- In the year 2005 django became open source under the BSD license.
- It was named Django, after the famous jazz guitarist Django Reinhardt.
- The django community rapidly grew, and the Django Software Foundation(DSF) was established in 2008 to maintain the project.
- The major websites Instagram, youtube, google, and The washington Post.


What are the advantges of django?
-----------------------------------------
1. Rapid development:
------------------------
- Django was designed with the intention to make a framework which takes less time to build web application.

2. Secure:
----------------------
- Django takes security seriously and helps developers to avoid many common security mistakes, such SQL injection
  attack.

3. Scalable:
-----------------
- Django is scalable in nature and has ability to quickly and flexibly switch from small to large application
  project.

4. Fully loaded:
----------------------
- Django includes various helping task modules and libraries which can be used to handle common web development
  tasks.


5. Open source:
--------------------
- Django is an open source web application framework. It is publicly available without cost.

6. It uses ORM(object relational mapper): By using this you can connect to the database without writing any sql
   query.

7. Versatile:
-----------------
- By using django you can build applications for different domains.
=================================================================================================================



How we can download django and create our first web application?
-------------------------------------------------------------------
- To install a django first visit to django official site https://www.djangoproject.com/download/
- Django rquires pip to start installation. Pip is package manager system which is used to install and manage
  packages written in python.

- For windows/Linux user you can use the command,
	pip install Django==5.2

- Once you install django,then go to your project location and type your first command to create django project.
	django-admin startproject first_django_app  (PyCharm)
         py -m django startproject first_django_app   (vscode)

- Once the project will created than go the location of first_django_app by using the command,
	cd first_django_app

- Once you enter into project location than create app using the command,
	python manage.py startapp myapp

- The manage.py file is very important file which can used for to create applications. It can also be used for
  different task like create the admin panel, it can be used to run your application.

- Once all the settings are done, then run your application using the command as below,
	python manage.py runserver

Django project Folder structure:
------------------------------------------------------------
1. manage.py:
-------------------------
- manage.py file is the most important file in django project.
- A command line tool that helps manage the django project.
- manage.py file can be used for to create the admin panal, it can also used for to run the server,
  it can also be used for migration process, it can be used for making the app.

Project level Files:
------------------------------
1. settings.py :
----------------------
- The heart of project configuration.
- The settings.py file can be used for to register the app in Installed apps
- The settings.py file can be used for to render html file as well static file(images,css, js)
- The settings.py file can be used for to make the database settings.


2. urls.py :
-------------------
- The urls.py file act as like router it means we can switch from one page to another page.
- This type urls we can mention in urls.py

Example :
------------------
http://localhost:8000/home
http://localhost:8000/about

In above url home, about these are called endpoints.

4. asgi.py :
-------------
ASGI = Asynchronous Server Gateway Interface
Entry point for running your project with ASGI capable servers.
By using this we can manage chatbox like application.

5. wsgi.py :
-------------------
WSGI --> Web server Gateway Interface
Used for deploying Django with production server.


App levels file:
----------------------------------
1. admin.py
2. models.py
3. views.py --> business logic

Q. How we can render html file using django?
----------------------------------------------------
1. create the django project using the command
    django-admin startproject projectname
py -m django startproject first_django_app   (vscode)
2. After creating the project enter into your project using the command
    cd projectname
3. When you enter in your project create app using the command,
    python manage.py startapp appname
4. When you create the app register the app inside settings.py under INSTALLED_APPS section.
5. When all the configuration done run the project using command,
    python manage.py runserver
6. create the folder at project level provide the name "templates"
7. When templates folder created then create another folder inside templates provide the name "myapp".
8. Inside the myapp folder create one html file name it as index.html
9. After completing the all step register the templates folder inside settings.py file.
    import os
    TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
10. Register the variable name TEMPLATE_DIR inside settings.py TEMPLATES section under
    DIR:[TEMPLATE_DIR]
11. Write down the bussiness logic inside the views.py file


    def Home(request):
    return render(request, "myapp/index.html")


12. Create the endpoint for that in your application level create one python file name as urls.py

    from django.urls import path
    from .views import *

    urlpatterns = [
            path('home/', Home, name="home"),
    ]
13. Include app level urls.py file inside project level urls.py file.

    from django.contrib import admin
    from django.urls import path,include

        urlpatterns = [
                path('admin/', admin.site.urls),
                path('',include('myapp.urls'))
       ]
14. Enter the url http://127.0.0.1:8000/home/









How we can use the CSS using Django?
============================================
1. If we want to render the CSS, js and images so we need to create one folder under our project that
   name is static folder.
2. Inside the static folder create another folder name it as CSS.
3. Inside the CSS folder create one file and that file name is style.css.
4. Register the static folder inside the settings.py file and add below code
    STATICFILES_DIRS = [
    BASE_DIR / "static",
    "/var/www/static/",
]

5. Go to the index.html file and at the starting you need write Django tag to load static file on this
   page. Write down the below code
   {% load static  %}

6. After writing the above code next we need to link CSS file in heading tag, as below
    <link rel="stylesheet" href="{% static 'css/style.css'  %}">




Q. How we can load the image file on page?
------------------------------------------------------------------
1. Create folder inside the static folder and provide name as per your choice.
2. Inside the index.html file write the code to attach image using img tag as below
    <img src="{% static 'images/watch.jpg'  %}" alt="watch" height="200" width="200">


Q. How we can attach bootstrap?
--------------------------------------

Q. What is mean by superuser?
---------------------------------------
- In django, a superuser is a special kind of user account that has all the permission and rights to
  the django admin site.

Q. What are key features of superuser in django?
-------------------------------------------------
1. Can log in to the django admin dashboard.
2. has full control over all models and data
3. can add, edit, delete and manage user and groups.




Q. How we can create superuser?
--------------------------------------------
We can create the superuser by using the following command,
    python manage.py createsuperuser

Before running the above command make sure you have connected to mysql database.
If not, then create one database in mysql and add database settings in settings.py file.
By, default django provide sqlite database to you.
Once you create the database add tables related with your project settings. You dont need to create
tables, django automatically create tables for you by using following command.
1. python manage.py makemigrations
2. python manage.py migrate



(   1 = pip install mysqlclient
    2 = python manage.py migrate
    3 = python manage.py createsuperuser
)

To solve no migration issue use below command,

To Fix Migration Issues in Django:
Reset app migrations (faking it):


1) python manage.py migrate myapp zero --fake

Re-apply migrations:


2) python manage.py migrate myapp





table bootstrap link:-


    <link rel="stylesheet" href="https://cdn.datatables.net/2.2.1/css/dataTables.bootstrap5.css">
    <link rel="stylesheet" href="https://cdn.datatables.net/responsive/3.0.3/css/responsive.bootstrap5.css">


    <script src="https://code.jquery.com/jquery-3.7.1.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdn.datatables.net/2.2.1/js/dataTables.js"></script>
    <script src="https://cdn.datatables.net/2.2.1/js/dataTables.bootstrap5.js"></script>
    <script src="https://cdn.datatables.net/responsive/3.0.3/js/dataTables.responsive.js"></script>
    <script src="https://cdn.datatables.net/responsive/3.0.3/js/responsive.bootstrap5.js"></script>



Session in Django
==========================
- A session is a way to store the information(data) about user across multiple requests.
- Session allow web applications to track and remember user interactions.
- In django session data is stored on the server side and associated with a unique session ID stored in the    						user's browser(usually as a cookie).

Where we use?
---------------------
1. Login authentication
2. shopping cart
3. Theme change(Dark/light)
4. Language settings

What are the advantages of session?
=========================================
1. Secure : Session data is stored on the server, not exposed to the client.
2. Persistent : Maintains user data across multiple pages until the session expires.
3. Customizable : You can set session expiration time.



Rest Framework using django
------------------------------------------------------
Backend deveeloper --> design the API's only
Frontend developer --> design the UI

1. Using the postman tool
2. Uisng inbuilt Restframework tool

Q. What is mean  by API?
----------------------------------------------------
- An API(Application programming interface) is a set of rule and protocols that allows different software applications to 
  communicate with each other.

Simple example
------------------------------------
Think of an API like a waiter in a hotel
1. You(client) tell the waiter(API) what you want(you request)
2. The waiter takes your order to the kitchen(server)
3. The kitchen prepares your food(data or service)
4. The waiter brings the food back to you(response).

Types API
---------------------------------
1. Web APIs(most common) :-> used over the internet(e.g Restful API)
2. Library APIs -> functions provided by libraries (e.g: Python math, os, datetime)
3. Operating System APIs :-> allow apps to interact with the os.


Common Terms
-----------------------------------
1. Client : Who is asking(your app)
2. Server : Who is giving the answer(the API backend)
3. Request : what the client sends.
4. Response : what the server sends back
5. EndPoint: a specific url where the API can be accessed.


Q. What is mean by Rest API?
------------------------------------------------------------
- A Rest API (Representational State Transfer API) is a type of web API that follows a set rules to allow communication between
  client (like web app or mobile) and server over the HTTP protocol.
  
- A Rest API lets you access or modify data over the server using standard http methods like,
a) GET : To read the data
b) POST : To add new data
c) PUT : Update data
d) DELETE : Delete the data
e) PATCH : Parital update

- Most Rest API use JSON format to send and receive the data.
- Each resource is accessed via a unique URL(called endpoint)

Q. What are the benefits of REST?
----------------------------------------------------------
1. Easy to use with any programming language.
2. Works with web application and mobile apps.
3. Scalable and fast




Serialization
--------------------
1. serialization class
2. Model Serializer

What is model serializer?
---------------------------
ModelSerializer is special serializer class in DRF that automatically creates serailizer fields based 
on a Django model.

When to use ModelSerailizer?
------------------------------
1. You are working with django Model
2. You want automatic field generation
3. You want automatic validations



Advantages of ModelSerializer
1. Clean and less code
2. Automatic validation
3. Integrates smoothly with Django models
4. Customizable when needed



Permission Classes ची थोडक्यात माहिती:
AllowAny: कोणालाही API access देता येतो (no authentication needed)

IsAuthenticated: फक्त लॉगिन केलेल्या यूजरसाठी API accessible आहे

IsAdminUser: फक्त admin यूजरसाठीच API accessible आहे


