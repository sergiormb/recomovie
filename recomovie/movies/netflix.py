from NetflixRoulette import *

def get_movie_netflix(title):
    try:
        movie = get_all_data(title)
        return movie
    except:
        return None
