from src.domain.Movie import *
from src.repository.MovieRepo import *

class MovieService:
    def __init__(self, movie_repo: MovieRepo):
        self.__repo = movie_repo

    def add_movie(self, movie):
        """
        Function that adds a movie to the list
        :param movie: object of type Movie
        :return:
        """
        self.__repo.add_movie(movie)

    def get_all_movies(self):
        """
        Function that returns the list of movies
        :return:
        """
        return  self.__repo.get_all_movies()

    def remove(self, movie_id: int):
        """
        Function that removes a movie
        :param movie_id: id of the movie to be removed
        :return:
        """
        self.__repo.remove(movie_id)

    def update_title(self, search_id: int, new_title):
        """

        :param search_id:
        :param new_title:
        :return:
        """
        self.__repo.update_title(search_id,  new_title)

    def update_description(self, search_id: int, new_description):
        """
        Function that updates the description of a movie
        :param search_id: id of the movie to be updated
        :param new_description: description that will replace the old one
        :return:
        """
        self.__repo.update_description(search_id, new_description)

    def update_genre(self, search_id: int, new_genre):
        """
        Function that updates the genre of a movie
        :param search_id: id of the movie to be updated
        :param new_genre: genre that will replace the old one
        :return:
        """
        self.__repo.update_genre(search_id, new_genre)

    def search(self, search_string: str):
        """
        Function that searches a movie by title
        :param search_string: string to be searched
        :return:
        """
        return self.__repo.search(search_string)

    def get_movie_by_id(self, id: int):
        """
        Function that returns a movie by id
        :param id: id of the movie to be returned
        :return:
        """
        return self.__repo.get_movie_by_id(id)

