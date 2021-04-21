from daos.movie_dao_impl import MovieDAOImpl
from daos.movie_dao_temp import MovieDAOTemp
from time import time

from exceptions.resource_unavailable import ResourceUnavailable


class MovieService:
    # movie_dao = MovieDAOTemp()
    movie_dao = MovieDAOImpl()

    @classmethod
    def create_movie(cls, movie):
        return cls.movie_dao.create_movie(movie)

    @classmethod
    def all_movies(cls):
        return cls.movie_dao.all_movies()

    @classmethod
    def get_movie_by_id(cls, movie_id):
        return cls.movie_dao.get_movie(movie_id)

    @classmethod
    def get_movie_above_price(cls, price):
        movies = cls.all_movies()

        refined_search = []

        for movie in movies:
            if movie["price"] >= price:
                refined_search.append(movie)

        return refined_search

    @classmethod
    def update_movie(cls, movie):
        # We should probably test that the movie_id exists in teh DB first. And throw ResourceNotFound if so.
        return cls.movie_dao.update_movie(movie)

    @classmethod
    def delete_movie(cls, movie_id):
        return cls.movie_dao.delete_movie(movie_id)

    @classmethod
    def checkout_movie(cls, movie_id):
        movie = cls.movie_dao.get_movie(movie_id)
        if movie.available:
            movie.available = False
            movie.return_date = int(time() + 604800)
            cls.update_movie(movie)
            return movie.title
        else:
            raise ResourceUnavailable(f"Movie is checked out. Expected return: {movie.return_date}")

    @classmethod
    def checkin_movie(cls, movie_id):
        movie = cls.movie_dao.get_movie(movie_id)
        if not movie.available:
            movie.available = True
            movie.return_date = 0
            cls.update_movie(movie)
            return movie.title
        else:
            raise ResourceUnavailable(f"Movie is not checked out. Cannot be checked in.")
