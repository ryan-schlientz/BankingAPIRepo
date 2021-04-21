class Movie:

    def __init__(self, movie_id=0, title="", genre="", price=0, available=True, return_date=0):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.price = price
        self.available = available
        self.return_date = return_date

    def json(self):
        return {
            'movieId': self.movie_id,
            'title': self.title,
            'genre': self.genre,
            'price': self.price,
            'available': self.available,
            'returnDate': self.return_date
        }

    @staticmethod
    def json_parse(json):
        movie = Movie()
        movie.movie_id = json["movieId"] if "movieId" in json else 0
        movie.title = json["title"]
        movie.genre = json["genre"]
        movie.price = json["price"]
        movie.available = json["available"] if "available" in json else True
        movie.return_date = json["returnDate"] if "returnDate" in json else 0

        return movie

    def __repr__(self):
        return str(self.json())
