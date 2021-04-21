from abc import abstractmethod, ABC


class MovieDAO(ABC):

    @abstractmethod
    def create_movie(self, movie):
        pass

    @abstractmethod
    def get_movie(self, movie_id):
        pass

    @abstractmethod
    def all_movies(self):
        pass

    @abstractmethod
    def update_movie(self, change):
        pass

    @abstractmethod
    def delete_movie(self, movie_id):
        pass
