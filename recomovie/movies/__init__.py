#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desarrollado por Sergio Pino Márquez
# 2016 email: sergiormb88@gmail.com
from django.conf import settings

from recomovie.movies.imdb import get_movie_imdb
from recomovie.movies.netflix import get_movie_netflix


class Movie(object):

    def __init__(
                self,
                title=None,
                netflix=False,
                imdb_id=None,
                description=None,
                poster=None,
                trailer=None,
                themoviedb_average=None,
                themoviedb_id=None,
                imdb_average=None,
                netflix_average=None,
                netflix_url=None,
                images=[]
                ):

        self.title = title
        self.description = description
        self.poster = poster
        self.trailer = trailer
        self.themoviedb_average = themoviedb_average
        self.themoviedb_id = themoviedb_id
        self.imdb_average = imdb_average
        self.imdb_id = imdb_id
        self.images = images
        self.netflix_average = netflix_average
        self.netflix_url = netflix_url

        super(Movie, self).__init__()

def get_list_movies(number):
    from recomovie.movies.themoviedb import TheMovieDbApi
    themoviedb = TheMovieDbApi()
    list_movies = themoviedb.get_random_top_250(number)
    for movie in list_movies:
        if movie.imdb_id:
            movie_imdb = get_movie_imdb(movie.imdb_id)
            movie.imdb_average = movie_imdb.imdb_rating
            movie_netflix = get_movie_netflix(movie_imdb.title)
            if movie_netflix:
                movie.netflix_average = movie_netflix['rating']
                movie.netflix_url = settings.NETFLIX_URL.format(show_id=movie_netflix['show_id'])
    return list_movies
