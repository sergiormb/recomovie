#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desarrollado por Sergio Pino Márquez
# 2015 email: sergiormb88@gmail.com

class Movie(object):

    def __init__(self, title=None, netflix=False, description=None, poster=None, trailer=None, imdb_rating=None, images=[]):
        self.title = title
        self.description = description
        self.poster = poster
        self.trailer = trailer
        self.imdb_rating = imdb_rating
        self.images = images
        self.netflix = netflix
        super(Movie, self).__init__()
