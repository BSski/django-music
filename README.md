
<p align="center">
  <h2 align="center">DjangoMusic</h2>
</p>


<div markdown="1" align="center">

[![Build Status](https://bsski.semaphoreci.com/badges/DjangoMusic/branches/main.svg?style=shields&key=db2ffdf5-30e8-46f6-83af-6960beb104fc)](https://bsski.semaphoreci.com/projects/DjangoMusic)
[![Demo Uptime](https://img.shields.io/uptimerobot/ratio/7/m791970415-adc4bd6d2b370b6f9fdce35f)](https://django-music-bsski.herokuapp.com/)
[![Heroku](https://pyheroku-badge.herokuapp.com/?app=django-music-bsski&style=flat)](https://django-music-bsski.herokuapp.com/)
[![Maintainability](https://api.codeclimate.com/v1/badges/b72dd7a07942d939db01/maintainability)](https://codeclimate.com/github/BSski/DjangoMusic/maintainability)
[![CodeFactor](https://www.codefactor.io/repository/github/bsski/djangomusic/badge)](https://www.codefactor.io/repository/github/bsski/djangomusic)
[![codecov](https://codecov.io/gh/BSski/DjangoMusic/branch/main/graph/badge.svg?token=Y21Z7RMYJL)](https://codecov.io/gh/BSski/DjangoMusic)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

</div>


<h3 align="center">
  :fireworks: Live demo :fireworks:
</h3>

<p align="center">
  https://django-music-bsski.herokuapp.com/
</p>



## Table of contents
* [Project description](#scroll-project-description)
* [Technologies used](#hammer-technologies-used)
* [Deployment](#hammer_and_wrench-deployment)
* [Features](#rocket-features)
* [Room for improvement](#arrow_up-room-for-improvement)
* [Author](#construction_worker-author)


## :scroll: Project description
This is a recruitment task for a Junior Python Developer position. The task was simple: to create a Django admin-panel-only website, with two models (Author, Song) with many-to-many relationship between them. The database choice was arbitrary, but with a recommendation of in-memory version. While I believe it would make the task easier in for example Java's Spring, it doesn't make it easier in Django. I decided to take the challenge and try to run Django with an in-memory database only and I succeeded. I do realise that it is a nonstandard solution, but I still wanted to try that, since the rest of the task was straightforward.
Besides that, I implemented automated testing in a CI/CD pipeline on SemaphoreCI, along with dockerization and deployment from a container to Heroku.


## :hammer: Technologies used
- Python 3.9.12
- Django 4.0.5
- Gunicorn 20.1.0
- Docker
- SemaphoreCI
- Heroku

## :hammer_and_wrench: Deployment

A) Docker image
1. Create an .env file basing on .env_sample_file from the repository.
2. Run `docker run --env-file .env -p 8020:8020 bsski/django-music:latest` in the .env file directory.
3. Access `localhost:8020`. 

B) without Docker
1. Download the repository.
2. Create an .env file basing on .env_sample_file from the repository in the directory of .env_sample_file.
3. Run `python manage.py runserver --noreload` in the directory of manage.py.
4. Access `127.0.0.1:8000`.

The admin panel can be found under your chosen URL or, if you didn't set it in the .env file, the default `/hidden_admin_url`.
Security through obscurity is not enough of course, but I find it a nice complementary solution.


## :rocket: Features
- two models in a many-to-many relationship (Author, Song)
- django admin panel which enables creating instances of models and viewing them
- purely in-memory database

Furthermore, the website is deployed on Heroku from a Docker image using a CI/CD SemaphoreCI pipeline:

![CI/CD screenshot](https://i.imgur.com/0NfYohr.png)


## :arrow_up: Room for improvement

Room for improvement:
- QoL features in admin panel could be added, for example sorting.


## :construction_worker: Author

- [@BSski](https://www.github.com/BSski)
