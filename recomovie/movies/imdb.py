#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desarrollado por Sergio Pino Márquez
# 2015 email: sergiormb88@gmail.com

import random
import requests
from django.conf import settings
from recomovie.movies import Movie


def size_str_to_int(x):
    return float("inf") if x == 'original' else int(x[1:])


class ImdbApi(object):

    def __init__(self, api_key=None, locale=None, anonymize=True,
                 exclude_episodes=None, user_agent=None, cache=None,
                 proxy_uri=None, verify_ssl=None):
        super(ImdbApi, self).__init__()
        self.locale = 'es_ES'
        self.caching_enabled = True
        self.anonymize = True
        # IMAGES
        self.the_movie_db_key = settings.THE_MOVIE_DB_KEY
        url = settings.THE_MOVIE_DB_CONFIG_PATTERN.format(key=self.the_movie_db_key)
        r = requests.get(url)
        config = r.json()
        if config.get('images', ''):
            self.base_url = config['images']['base_url']
            sizes = config['images']['poster_sizes']
            """
                'sizes' should be sorted in ascending order, so
                max_size = sizes[-1]
                should get the largest size as well.
            """
            self.max_size_poster = max(sizes[2:4], key=size_str_to_int)
            self.max_size_photos = max(sizes[2:5], key=size_str_to_int)
            self.max_size_cast = max(sizes[1:2], key=size_str_to_int)

    def get_movie_video(self, imdb_id):
        response = requests.get(settings.VIDEO_URL.format(key=self.the_movie_db_key, imdbid=imdb_id))
        api_response = response.json()
        results = api_response.get('results', None)
        if results:
            results = results
            video = results[0]
            return video['key']
        else:
            return None

    def get_movie_cast(self, imdb_id):
        response = requests.get(settings.CREDITS_URL.format(key=self.the_movie_db_key, imdbid=imdb_id))
        api_response = response.json()
        cast = api_response['cast']
        for actor in cast[:4]:
            actor['url_image'] = "{0}{1}{2}".format(self.base_url, self.max_size_cast, actor['profile_path'])
        return cast[:4]

    def get_movie_images(self, imdb_id):
        response = requests.get(settings.IMG_PATTERN.format(key=self.the_movie_db_key, imdbid=imdb_id))
        api_response = response.json()
        images_movie = {}
        # POSTER
        api_poster = api_response.get('posters', None)
        if api_poster:
            posters = api_poster
            poster = posters[0]
            rel_path = poster['file_path']
            url = "{0}{1}{2}".format(self.base_url, self.max_size_poster, rel_path)
            images_movie['poster'] = url
        # IMAGES
        api_backdrops = api_response.get('backdrops', None)
        if api_backdrops:
            backdrops = api_backdrops
            backdrops_urls = []
            for backdrop in backdrops[:8]:
                rel_path = backdrop['file_path']
                url = "{0}{1}{2}".format(self.base_url, self.max_size_photos, rel_path)
                backdrops_urls.append(url)
            images_movie['photos'] = backdrops_urls
        return images_movie

    def get_movie_complete(self, movie):
        movie['images'] = self.get_movie_images(movie['id'])
        # movie['cast'] = self.get_movie_cast(movie['id'])
        trailer = self.get_movie_video(movie['id'])
        if trailer:
            movie['trailer'] = trailer
        return movie

    def get_random_top_250(self, number=1):
        response = requests.get(settings.DISCOVER_URL.format(key=self.the_movie_db_key))
        api_response = response.json()
        results = api_response.get('results', '')
        movies = []
        if results:
            titles_movies = []
            while (len(movies) < number):
                movie_result = random.choice(results)
                movie_result = self.get_movie_complete(movie_result)
                movie = Movie(
                    title=movie_result['title'].encode("utf-8"),
                    description=movie_result['overview'].encode("utf-8"),
                    imdb_rating=movie_result['popularity'],
                    trailer=movie_result.get('trailer', None),
                )
                if movie_result.get('images', ''):
                    movie.poster = movie_result['images']['poster']
                    movie_result['images']['photos']
                if movie.title not in titles_movies:
                    movies.append(movie)
                    titles_movies.append(movie.title)
        return movies

    def get_random_genre(self, genre):
        genre = Genre.objects.filter(name__contains=genre)
        response = requests.get(settings.GENRE_URL.format(key=self.the_movie_db_key, genre=genre[0].api_id))
        api_response = response.json()
        results = api_response['results']
        movie = random.choice(results)
        movie = self.get_movie_complete(movie)
        return movie
