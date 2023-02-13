# DSC 180 B16 - Decentralized Location Consensus

Group Members:  
Alan Miyazaki  
Alex Guan  
Mason Chan  
Nathan Ahmann  

[Video Demo](https://youtu.be/Ixj5MV3JIbA) that shows the server working with GET and POST requests.

## Content

This repository contains all the files sent to our Heroku server which can be accessed [here](https://dsc180-decentralized-location.herokuapp.com/).  

This main server has the API for the backend and a landing page for the website. In the final version, an Android device will send get/post requests to this backend which will allow the app to verify the location of users. The verification is done via blacklisting malicious users by having Heroku run `trust_algorithm.py` on a set timer. This file updates the database for the blacklist on the backend.


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
