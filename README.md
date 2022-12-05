# DSC 180A - Decentralized Location Consensus
Section B16  

Group Members:  
Alan Miyazaki  
Alex Guan  
Mason Chan  
Nathan Ahmann  

[Video Demo](https://youtu.be/Ixj5MV3JIbA) that shows the server working with GET and POST requests.

## Content

This repository contains all the files sent to our Heroku server which can be accessed [here](https://dsc180-decentralized-location.herokuapp.com/).  
This website functions as a webservice backend to our decentrailized location consensus application, that the other team in our section is creating for Android.

If you would like to run this website locally, you can install the necessary packages and run the following code in the terminal. Note that the local development version of the server utilizes sqlite3 as the database since it is easier to locally utilize than Postgres which we use on our Heroku server.

`python manage.py makemigrations` - sets up the migrations for the database
`python manage.py migrate` - makes the migration files
`python manage.py runserver` - will run the server which can then be accessed at 127.0.0.1


## Contains parts of code modified from the following tutorials:
https://docs.djangoproject.com/en/4.1/intro/   
https://github.com/heroku/python-getting-started  
https://devcenter.heroku.com/articles/getting-started-with-python  
https://www.django-rest-framework.org/tutorial/quickstart/   
https://www.django-rest-framework.org/tutorial/1-serialization/  

