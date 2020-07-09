# Django-Recipe-API

A REST-Full API built with Django Rest Framework. The API will retrieve recipes and ingredients needed for the particular recipe with user authentication and authentication handling. 


![Django Rest Framework](https://files.realpython.com/media/djang-rest-framework-logo.37921ea75c09.png)


[![Build Status](https://travis-ci.com/memetics19/Django-Recipe-API.svg?branch=master)](https://travis-ci.com/memetics19/Django-Recipe-API)
[![CircleCI](https://circleci.com/gh/circleci/circleci-docs.svg?style=svg)](https://cirrus-ci.com/build/6236223771508736)
[![License](http://img.shields.io/:license-mit-blue.svg)](http://doge.mit-license.org)
![GitHub closed issues](https://img.shields.io/github/issues-closed/memetics19/Django-recipe-api)
![GitHub pull requests](https://img.shields.io/github/issues-pr/memetics19/Django-Recipe-API)
![GitHub followers](https://img.shields.io/github/followers/memetics19?style=social)
![GitHub stars](https://img.shields.io/github/stars/memetics19/django-recipe-api?style=social)

# How to Setup the Local Server 

1. Clone the Repo by following command
  `git clone git@github.com:memetics19/Django-Recipe-API.git` .
  if you haven't add ssh key probably add by clicking this <a href = "https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh">link</a>

2. Install Docker if you haven't installed it, yet. You can install by clicking this  <a href="https://www.docker.com/">link</a>

3. Use this command to install the dependencies 
   `docker-compose build`
4. Use this command to run the server 
   `docker-compose up`
5. Navigate to `127.0.0.1:5000`

# API Endpoints
`api/auth/create` 

`api/auth/token`

# Planning - TO DO
 
To know what's the further development of the project Check <a href = "TODO/Notes.md">Notes</a>

# Dependencies

1. Django 
2. DjangoRestFrameWork
3. Flake8

# Note
Docker does'nt work on Windows 10 Home Edition 
