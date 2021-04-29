# Exam-Portal

## Overview
A complete Exam Portal System built using Django. Currently, the portal has login system(with authentication) for admin(the top level supervisor), professors and students with their respective homepage; MCQ questions, question papers, student groups and exams can be created/edited by professors; students can appear for exams allotted to them within the time constraints set by the professor and then view their marks and solutions after completing the exam.

## Running
For running the project, navigate to the project directory and follow the following instructions:

* Type the following in the command line(remaining inside the virtual environment):
    * python manage.py makemigrations
    * python manage.py migrate
    * python manage.py createsuperuser - this will ask for username, email(optional) and password. Enter some credentials to be used later for django admin functionality.
    * python manage.py runserver

* Log on to [django admin site](http://127.0.0.1:8000/admin) using the superuser credentials
    * Click on **Groups** section and create 2 groups - ***Professor*** and ***Student***
    * Click on **Users** section and create some users, and also make each user belong to one of the groups- Professor/Student as per role
    * Logout of the admin site and go to http://127.0.0.1:8000/ where the home page of the project will be rendered.

* Now any student/professor can login using their own credentials.
* This project is made by students of SRM Institute,CSE F
