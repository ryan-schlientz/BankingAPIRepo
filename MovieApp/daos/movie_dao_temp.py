from daos.movie_dao import MovieDAO
from exceptions.resource_not_found import ResourceNotFound
from util.temp_db import TempDB as db


class MovieDAOTemp(MovieDAO):

    def create_movie(self, movie):
        db.movies[movie.movie_id] = movie

    def get_movie(self, movie_id):
        try:
            return db.movies[movie_id]
        except KeyError:
            raise ResourceNotFound(f"Movie with id: {movie_id} - Not Found")

    def all_movies(self):
        # return [movie.__dict__ for movie in db.movies.values()]
        return [movie.json() for movie in db.movies.values()]

    def update_movie(self, change):
        db.movies.update({change.movie_id: change})

    def delete_movie(self, movie_id):
        del db.movies[movie_id]
