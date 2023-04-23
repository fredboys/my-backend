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

# Agile Methodology
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

By using AGILE methodology in this project I was able to deliver a site which had all required functionality and was able to give even more extra detail when going through the project.

[Project Board Link](https://github.com/users/fredboys/projects/11)
![Project Board](/readme/projectboard-cm.jpg)

# CRUD Functionality

Full CRUD Functionality has been used in this project

Create - Users can create profiles, posts, comments, votes and favourites
Read - User can view all product posts, favourites, votes and comments
Update - Users can update posts, comments, votes, favourites and profile details
Delete - Users can update posts, comments, votes and favourites

# Database Design

Database diagram shows the relationship between all the apps that have been created during this project.

![Database diagram](/readme/database-cm.jpg)

# Security

A permissions class was added called IsOwnerOrReadOnly to ensure only users who create the content are able to edit or delete it.

# Technology

# Testing 

# Deployment
## Heroku
## Locally
## Fork

# Credits
## Content
## Acknowledgements