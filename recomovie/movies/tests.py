# -*- coding: utf-8 -*-
'''
    File name: test.py
    Author: Peter Test
    Date created: 4/20/2013
    Date last modified: 4/25/2013
    Python Version: 2.7
'''

from django.test import TestCase
from recomovie.movies.themoviedb import TheMovieDbApi


class TheMovieDbTest(TestCase):
    """Comprobamos que la API de TheMovieDb funciona correctamente."""

    def setUp(self):
        """Prueba de la longitud de la lista aleatoria de peliculas."""
        self.len = 6

    def tearDown(self):
        """Prueba de la longitud de la lista aleatoria de peliculas."""
        del self.len

    def test_len_random_top(self):
        """Prueba de la longitud de la lista aleatoria de peliculas."""
        themoviedb = TheMovieDbApi()
        list_movies = themoviedb.get_random_top_250(self.len)
        self.assertEqual(len(list_movies), self.len)

    def test_repeat_random_top(self):
        u"""Prueba de que no exista ninguna pelicula.

        repetida en la lista aleatoria de peliculas.
        """
        themoviedb = TheMovieDbApi()
        list_titles = []
        list_movies = themoviedb.get_random_top_250(self.len)
        for movie in list_movies:
            list_titles.append(movie.title)
        self.assertEqual(len(list_movies), len(set(list_titles)))
