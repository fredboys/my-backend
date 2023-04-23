# Compare Mate API 

Compare Mate API is the backend service used by the [Compare Mate application](https://github.com/fredboys/compare-mate)



# Content

* [Development Goals](#development-goals)
* [Agile Methodology](#Agile-methodology)
    * [User Stories](#user-stories)
    * [Project Board](#project-board)
* [Database Design](#database-design)
* [API End Points](#api-end-points)
* [Security](#security)
* [Technology](#technology)
* [Packages](#packages)
* [Testing](#testing)
* [CRUD Functionality](#crud-functionality)
* [Deployment](#deployment)
    * [Heroku](#heroku)
    * [Locally](#locally)
    * [Fork](#fork)
* [Credits](#Credits)
    * [Content](#content)
    * [Acknowledgements](#acknowledgements)







# Development Goals

The goal of this application was to host the backend database for the frontend application "Compare Mate". It has been designed to allow full CRUD functionality across the platform via the user interface

# Agile Methodology

By using AGILE methodology in this project I was able to deliver a site which had all required functionality and was able to give even more extra detail when going through the project. It had been done by delivering small features in incremental sprints. This was done with a tight deadline only being less then a month away.

## User stories

As a developer: 

* I need to create the base project set up so that I can build out the features.
*  I need to connect cloudinary to the project so that static images can be uploaded by users and hosted there.
*  I need to allow users to register and sign in securely with All Auth so that they can browse the site safely.
* I need to create a product View so that allow users to be able to see all products that are being posted and allow them to create their own.
*  I need to allow the user to be able to edit and delete their product posts so that they can change any errors they made when it was first created
* I want to create a new blank profile with default image when a user is created.
*  I need create a favourite app so that users can save products for later
*  I need to create a comment app so that users can share thoughts and build a community
*  I need to create a category list for products so that the products are easily attainable by others
* I need to create a Up Vote app so that I can provide a trending products section
* I need to be able to access the admin panel to delete users or products so that I can delete any inappropriate content
*  I need to create and access the contact form from the admin so that I can review any feedback so that I can improve the site.


## Project Board

Githubs projects was used to track user stories and implement ideas based on their level of importance for allowing use of the app with no loss of functionality or user experience. Two labels were created indicating their level of importance, those were:

* Must Have 
* Should Have

[Project Board Link](https://github.com/users/fredboys/projects/11)
![Project Board](/readme/projectboard-cm.jpg)

# CRUD Functionality

Full CRUD Functionality has been used in this project

* Create - Users can create profiles, posts, comments, votes and favourites
* Read - User can view all product posts, favourites, votes and comments
* Update - Users can update posts, comments, votes, favourites and profile details
* Delete - Users can update posts, comments, votes and favourites

# Database Design

Database diagram shows the relationship between all the apps that have been created during this project.

![Database diagram](/readme/database-cm.jpg)

# API End Points

Contacts

End point: /contacts/

* POST - To create contact request
* GET - To get a list of contact requests

End point: /contacts/int:pk/

* PUT - To update a single contact request
* GET - To get a single contact request
* DELETE - To delete a contact request

Products

End point: /products/

* POST - To create a product post
* GET - To list the product posts 

End point: /products/int:pk/

* PUT - To update a single post
* GET - To get a single post
* DELETE - To delete a post

Profiles

End point: /profiles/

* POST - To create a profile
* GET - To list the profiles 

End point: /profiles/int:pk/

* PUT - To update a single profile
* GET - To get a single profile
* DELETE - To delete a profile

Comments

End point: /comments/

* POST - To create a comment
* GET - To list the comments

End point: /comments/int:pk/

* PUT - To update a single comment
* GET - To get a single comment
* DELETE - To delete a comment

Favourite

End point: /favourite/

* POST - To create a favourite on a product
* GET - To list the favourites

End point: /favourite/int:pk/

* PUT - To update a favourite
* GET - To get a single favourite
* DELETE - To delete a favourite

Vote

End point: /votes/

* POST - To create a vote on a product
* GET - To list the votes

End point: /votes/int:pk/

* PUT - To update a vote
* GET - To get a single vote
* DELETE - To delete a vote

# Security

A permissions class was added called IsOwnerOrReadOnly to ensure only users who create the content are able to edit or delete it.

All necessary secret variables were stored in the env.py file.

# Technology

* Django
    * Main framework used for application creation

* Django REST Framework
    * Framework used for creating API

* Cloudinary
    * Used for static image hosting

* Heroku
    * Used for hosting the application

* ElephantSql
    * Used for hosting database

* Git 
    * Used for version control

* GitHub
    * Repository for storing code

# Packages

* asgiref==3.6.0
* cloudinary==1.32.0
* dj-database-url==0.5.0
* dj-rest-auth==2.1.9
* Django==3.2.18
* django-allauth==0.44.0
* django-cloudinary-storage==0.3.0
* django-cors-headers==3.14.0
* django-filter==23.1
* djangorestframework==3.14.0
* djangorestframework-simplejwt==5.2.2
* gunicorn==20.1.0
* oauthlib==3.2.2
* Pillow==9.5.0
* psycopg2==2.9.6
* PyJWT==2.6.0
* python3-openid==3.2.0
* pytz==2023.3
*  requests-oauthlib==1.3.1
* sqlparse==0.4.3


# Testing 

All folders were run through flake8. Several issues appeared with various reasons, lines too long, blank spaces, no new line.

All issues were resolved with the exception of lines too long in migration files (these are auto generated so I did not fix) and the auth validator lines in the settings.py which seem to be unbreakable but are framework code.

A warning appeared for env.py being imported but unused although this is being used in the development version, so this was ignored.

* Comments

![comments test](/readme/commenttest-cm.jpg)

* Contacts

![contacts](/readme/contactstest-cm.jpg)

* Drf_api

![drf_api](/readme/drf_apitest-cm.jpg)

* Favourite

![favourite](/readme/favouritetest-cm.jpg)

* Products

![products](/readme/productstest-cm.jpg)

* Profile

![profiles](/readme/profilestest-cm.jpg)

* Votes

![votes](/readme/votestest-cm.jpg)

# Deployment
## Heroku

The site was deployed to Heroku. The steps to deploy are as follows:

* Navigate to heroku and create an account
* Click the new button in the top right corner
* Select create new app
* Enter app name
* Select region and click create app
* Click the resources tab and search for Heroku Postgres
* Select hobby dev and continue
* Go to the settings tab and then click reveal config vars
* Add the following config vars:
    * SECRET_KEY: (Your secret key)
    * DATABASE_URL: (From your ElephantSql)
    * ALLOWED_HOST:
    * CLIENT_ORIGIN: url for the client front end react application that will be making requests to these APIs
    * CLIENT_ORIGIN_DEV: address of the local server used to preview and test UI during development of the front end client application
    * CLOUDINARY: (Your cloudinary link)
    * DISABLE_COLLECTSTATIC: 1
* Click the deploy tab
* Scroll down to Connect to GitHub and sign in / authorize when prompted
* In the search box, find the repositoy you want to deploy and click connect
* Scroll down to Manual deploy and choose the main branch
* Click deploy

## Locally

Navigate to the GitHub Repository you want to clone to use locally:

* Click on the code drop down button
* Click on HTTPS
* Copy the repository link to the clipboard
* Open your IDE of choice (git must be installed for the next steps)
* Type git clone copied-git-url into the IDE terminal

The project will now have been cloned on your local machine for use.

In order to run, you will need to create an env.py file and add the config vars as used in heroku steps above.

## Fork

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.

* Navigate to the GitHub Repository you want to fork.
* On the top right of the page under the header, click the fork button.
* This will create a duplicate of the full project in your GitHub Repository.

# Credits
## Content

[Choices field](https://stackoverflow.com/questions/18676156/how-to-properly-use-the-choices-field-option-in-django) - I used this link to help me with the category drop down for my products

## Acknowledgements

Than you to my mentor Daisy for helping me through this project.