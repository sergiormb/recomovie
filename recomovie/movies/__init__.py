#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desarrollado por Sergio Pino Márquez
# 2016 email: sergiormb88@gmail.com
from django.conf import settings

from recomovie.movies.imdb import get_movie_imdb
from recomovie.movies.netflix import get_movie_netflix
from recomovie.movies.filmaffinity import get_average_movie_filmaffinity


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
                tomatoes_average=None,
                filmaffinity_average=None,
                photo=None,
                ):

        self.title = title
        self.description = description
        self.photo = photo
        self.poster = poster
        self.trailer = trailer
        self.themoviedb_average = themoviedb_average
        self.themoviedb_id = themoviedb_id
        self.imdb_average = imdb_average
        self.imdb_id = imdb_id
        self.netflix_average = netflix_average
        self.netflix_url = netflix_url
        self.tomatoes_average = tomatoes_average
        self.filmaffinity_average = filmaffinity_average

        super(Movie, self).__init__()

def get_list_movies(number):
    from recomovie.movies.themoviedb import TheMovieDbApi
    themoviedb = TheMovieDbApi()
    list_movies = themoviedb.get_random_top_250(number)
    for movie in list_movies:
        if movie.imdb_id:
            movie_imdb = get_movie_imdb(movie.imdb_id)
            movie.imdb_average = movie_imdb.imdb_rating
            movie.tomatoes_average = movie_imdb.tomato_rating
            movie_netflix = get_movie_netflix(movie_imdb.title)
            if movie_netflix.is_on_netflix:
                movie.netflix_average = movie_netflix.rating
                movie.netflix_url = settings.NETFLIX_URL.format(show_id=movie_netflix.show_id)
            movie.filmaffinity_average = get_average_movie_filmaffinity(movie.title)
    return list_movies
