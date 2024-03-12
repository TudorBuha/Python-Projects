import random


class Movie:
    def __init__(self, movie_id:int, title:str, description:str, genre:str):
        self.__movie_id=movie_id
        self.__title=title
        self.__description=description
        self.__genre=genre

    @property
    def movie_id(self):
        return self.__movie_id
    @property
    def title(self):
        return self.__title
    @property
    def description(self):
        return self.__description
    @property
    def genre(self):
        return self.__genre
    @movie_id.setter
    def movie_id(self, new_movie_id):
        self.__movie_id=new_movie_id
    @title.setter
    def title(self, new_title):
        self.__title=new_title
    @description.setter
    def description(self, new_description):
        self.__description=new_description
    @genre.setter
    def genre(self, new_genre):
        self.__genre=new_genre
    def __str__(self):
        return("movie id: "+ str(self.__movie_id) + " | title: " + str(self.__title) + " | description: " + str(self.__description)+ " | genre: " + str(self.__genre))