Recomovie
=================

[![Build Status](https://travis-ci.org/sergiormb/recomovie.svg?branch=master)](https://travis-ci.org/sergiormb/recomovie)
[![Coverage Status](https://coveralls.io/repos/github/sergiormb/recomovie/badge.svg?branch=master)](https://coveralls.io/github/sergiormb/recomovie?branch=master)

This is an application created with the Django framework with the motive to keep learning new things. If you visit the application, it will recommend movies at random according valuations IMDB, Netflix, etc. It features:

* Integration with IMDB
* Translation of the summary and display of the trailers in Spanish

Requirements
============

**Django 1.10**

Installation
============

1. ``pip install -r requirements.txt``
2. add ``"THE_MOVIE_DB_KEY"`` to ``settings_local.py`` You can get the key in https://www.themoviedb.org/documentation/api

Usage
=====

1. ``python manage.py syncdb``
2. ``python manage.py collectstatic``
3. ``python manage.py runserver``
