
# FT-Test
An API built with Django framework to return user activities in JSON form.
------------

##### The API is live at -
### [PythonAnywhere](http://snusc.pythonanywhere.com/api/ "PythonAnywhere link") and [Heroku](https://ft-api-00.herokuapp.com/api/ "Heroku link")
 - http://snusc.pythonanywhere.com/api/
 - https://ft-api-00.herokuapp.com/api/
 ------------
### Features -
  - User activity tracking
  - JWT login and signup
  - Ready to deploy API
  - Customized admin panel with detailed view of model objects
  - Possesses Custom Management Command to fill in dummy data
  - Abiding with PEP8 and strictly abiding with DRY principle
 

------------
## Table of Contents
1) [Getting Started](#getting-started)
2) [Usage](#usage)
3) [RESTful Structure](#restful-structure)
4) [Custom Management Command](#custom-management-command)
5) [Screenshots](#screenshots)
6) [Deployment - VPS and PaaS](#deployment-vps-and-paas)
7) [Modules and packages Used](#modules-and-packages-used)
8) [Repository Map](#repository-map)
9) [Repository Guide](#respository-guide)

# Getting Started

  - Clone the repository
  - Create a virtual env and activate it
  - Go to the project directory and Install the required modules using
```sh
pip install -r requirements.txt
```
- Run the following command in terminal
```sh
python manage.py makemigrations profiles_api
python manage.py migrate --run-syncdb
```
- Run the server
```sh
python manage.py runserver
```



## Usage
 >NOTE - Its recommended to run the server at least once before filling in dummy data so that django created the sqlite database.
- Now, the database won't be having any data, so populate the database with dummy data using the following command
```sh
python manage.py floodTheDB
```
- This command will add dummy users and their activity data automatically.
- Now go to 
```sh
http://127.0.0.1:8000/api
```
- You'll see this
![](https://i.ibb.co/1Xgg8jM/api-Root-min.jpg)
- Navigate to any of the endpoints through here or directly reach to an endpoint through the links below

> List of User Profiles - http://snusc.pythonanywhere.com/api/profile/ or https://ft-api-00.herokuapp.com/api/profile/

> List of User Activities - http://snusc.pythonanywhere.com/api/user-activity/ or https://ft-api-00.herokuapp.com/api/user-activity/

- Connect your frontend to any of these endpoints to carry out your operations. The possible responses are tabularized below.

# RESTful Structure

| EndPoint  | HTTP Method  | CRUD Method | Result |
| :------------ |:---------------:| -----:| -----:|
| http://127.0.0.1:8000/api/   | GET | READ |  Gets the list of endpoints  |
| http://127.0.0.1:8000/api/user-activity/     | GET        |   READ | Gets the user's name and their activities  |
| http://127.0.0.1:8000/api/profile/  | POST       |    CREATE |     Create a new user| 
| http://127.0.0.1:8000/api/profile/  | GET       |   READ |     Get all users list| 
| http://127.0.0.1:8000/api/profile/:id  | POST       |   UPDATE |     Update logged in user's info| 
| http://127.0.0.1:8000/api/profile/:id  | GET       |   READ |     Get a particular user info| 

## Custom Management Command
- The project possesses a custom management command to populate the database with dummy data
- Run the command using the following code
`python manage.py floodTheDB`
- The command also supports an optional argument  `--delete-existing` to delete the existing data before populating it
`python manage.py floodTheDB --delete-existing`

>NOTE - The flooder might give Runtime warning but that problem won't interfere with the project at current stage.


## Screenshots
##### User Activities endpoint
![](https://i.ibb.co/Pgb4S7w/useract.jpg)
##### User Profiles endpoint
![](https://i.ibb.co/yNbF38z/userprofile.jpg)
##### Admin Panel
![](https://i.ibb.co/bH2cR0S/activityperiods.jpg)
![](https://i.ibb.co/9qkHmSm/Users.jpg)

## Deployment
> You might need to play a little bit with `STATIC_ROOT` and other static files depending on the providers.
- The packages required for deployment are already included in `reuquirements.txt`
- The guide to deploy the project to VPS and PaaS is given below
#### For VPS (eg. Digital Ocean, AWS)
- Clone the repo
`git clone https://github.com/SahilChoudhary22/ft-project`
- Edit the `ALLOWED_HOSTS` in `settings.py` according to your hosting service
- It's advised to create a `local_settings.py` file containing your sensitive information.
- Voila! You're up!

#### For PaaS (eg. Heroku)

> PaaS usually provide a way for you to change your `settings.py` variables later. So you probably won't need to create a different file for sensitive information like you did in VPS.
- Git method - 
- Initialise git repo and Add git remote to your chosen provider.
- Push the project up
`git push <provider> master`
- Voila! You're up


> IMPORTANT NOTES - Test case weren't added and SQLite DB is the default DB of the project due to time concern. Security Key, DEBUG other sensitive information is intentionally left as it is. However, it's using PostgreSQL on Heroku.

------------
## Python packages/modules used

```
asgiref==3.2.7
dj-database-url==0.5.0
Django==3.0.6
django-heroku==0.3.1
djangorestframework==3.11.0
Faker==4.1.0
gunicorn==20.0.4
psycopg2==2.8.5
python-dateutil==2.8.1
pytz==2020.1
six==1.15.0
sqlparse==0.3.1
text-unidecode==1.3
whitenoise==5.1.0 
```
Out of these, whitenoise, gunicorn and dj-database-url are for deployment. You won't need them if you're testing the app on local server.

## Repository Map 
```sh
https://github.com/SahilChoudhary22/ft-project
|   .gitignore  
|   manage.py
|   Procfile
|   README.md
|   requirements.txt
|   runtime.txt
|   
+---ft_project
|   |   asgi.py
|   |   settings.py
|   |   urls.py
|   |   wsgi.py
|   |   __init__.py
|   |   
|   +---staticfiles
|
|           
\---profiles_api
    |   admin.py
    |   apps.py
    |   models.py
    |   permissions.py
    |   serializers.py
    |   tests.py
    |   urls.py
    |   views.py
    |   __init__.py
    |   
    +---management
        \---commands
                floodTheDB.py
                __init__.py
```

## Repository Guide
| File/folder name  | What is this? |
| :------- |:-------:|
| ft_project | django project name |
| profiles_api | django application name |
| Procfile | Used by heroku |
|runtime.txt | contains python version |
