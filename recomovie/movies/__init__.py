#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desarrollado por Sergio Pino Márquez
# 2015 email: sergiormb88@gmail.com
from recomovie.movies.imdb import get_average_imdb


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
        self.netflix = netflix

        super(Movie, self).__init__()

def get_list_movies(number):
    from recomovie.movies.themoviedb import TheMovieDbApi
    themoviedb = TheMovieDbApi()
    list_movies = themoviedb.get_random_top_250(number)
    for movie in list_movies:
        if movie.imdb_id:
            movie.imdb_average = get_average_imdb(movie.imdb_id)
    return list_movies
