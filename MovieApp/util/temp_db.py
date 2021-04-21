from models.movie import Movie


# This is temporary code I am showing you as a way to have functionality without worrying
# about data persistence quite yet.

class TempDB:
    movies = {
        1: Movie(movie_id=1, title="The Avengers", genre="Action", price=5, available=True, return_date=0),
        2: Movie(movie_id=2, title="Iron Man", genre="Action", price=4.5, available=True, return_date=0),
        3: Movie(movie_id=3, title="Thor", genre="Action", price=4.5, available=True, return_date=0)
    }
