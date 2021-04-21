from daos.movie_dao import MovieDAO
from exceptions.resource_not_found import ResourceNotFound
from models.movie import Movie
from util.db_connection import connection


class MovieDAOImpl(MovieDAO):

    def create_movie(self, movie):
        sql = "INSERT INTO movies VALUES (DEFAULT,%s,NULL,%s,%s,DEFAULT,NULL) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (movie.title, movie.price, movie.available))

        connection.commit()
        record = cursor.fetchone()

        new_movie = Movie(record[0], record[1], record[2], float(record[3]), record[4], record[5])
        return new_movie

    def get_movie(self, movie_id):
        sql = "SELECT * FROM movies WHERE id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [movie_id])

        record = cursor.fetchone()

        if record:
            return Movie(record[0], record[1], record[2], float(record[3]), record[4], record[5])
        else:
            raise ResourceNotFound(f"Movie with id: {movie_id} - Not Found")

    def all_movies(self):
        sql = "SELECT * FROM movies"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        movie_list = []

        for record in records:
            movie = Movie(record[0], record[1], record[2], float(record[3]), record[4], record[5])

            movie_list.append(movie.json())

        return movie_list

    def update_movie(self, change):
        sql = "UPDATE movies SET title=%s,price=%s,available=%s,return_date=%s WHERE id = %s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (change.title, change.price, change.available, change.return_date, change.movie_id))
        connection.commit()

        record = cursor.fetchone()

        new_movie = Movie(record[0], record[1], record[2], float(record[3]), record[4], record[5])
        return new_movie

    def delete_movie(self, movie_id):
        sql = "DELETE FROM movies WHERE id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [movie_id])
        connection.commit()


def _test():
    m_dao = MovieDAOImpl()
    movies = m_dao.all_movies()
    print(movies)

    print(m_dao.get_movie(1))


if __name__ == '__main__':
    _test()
