from numpy import random
import pickle

from src.domain.Movie import Movie

class NotUniqueMovieIdError(Exception):
    def __init__(self, movie_id):
        self.__movie_id = movie_id

    def __str__(self):
        return str(self.__movie_id) + " is not an unique movie id "

class NotFoundError(Exception):
    def __init__(self, entity_id):
        self.__entity_id = entity_id
    def __str__(self):
        return str(self.__entity_id) + " this id is not found"
class MovieRepo:

    def __init__(self):
        self._movielist = []
        self.generate_n_movies(20)

    def add_movie(self, movie:Movie):
        """
        Function that adds a movie to the list
        :param movie: object of type Movie
        :return:
        """
        if self.already_exists_movie(movie) is False:
            raise NotUniqueMovieIdError(movie.movie_id)



        self._movielist.append(movie)
    def get_all_movies(self):
        """
        Function that returns the list of movies
        :return:
        """
        return self._movielist

    def update_title(self, search_id, new_title):
        """
        Function that updates the title of a movie
        :param search_id: id of the movie to be updated
        :param new_title: new title that will replace the old one
        :return:
        """
        found=0
        for movie in self._movielist:
            if search_id == movie.movie_id:
                movie.title = new_title
                found=1
        if found==0:
            raise  NotFoundError(search_id)

    def update_description(self, search_id, new_description):
        """
        Function that updates the description of a movie
        :param search_id: id of the movie to be updated
        :param new_description: description that will replace the old one
        :return:
        """
        found=0
        for movie in self._movielist:
            if search_id == movie.movie_id:
                movie.description = new_description
                found=1
        if found==0:
            raise NotFoundError(search_id)


    def update_genre(self, search_id, new_genre):
        """
        Function that updates the genre of a movie
        :param search_id: id of the movie to be updated
        :param new_genre: genre that will replace the old one
        :return:
        """
        found=0
        for movie in self._movielist:
            if search_id == movie.movie_id:
                movie.genre = new_genre
                found=1
        if found==0:
            raise NotFoundError(search_id)


    def remove(self, movie_id):
        """
        Function that removes a movie
        :param movie_id: id of the movie to be removed
        :return:
        """
        found=0
        for movie in self._movielist:
            if movie_id == movie.movie_id:
                self._movielist.remove(movie)
                found=1
        if found==0:
            raise NotFoundError(movie_id)

    def search(self, search_string: str):
        """
        Function that searches for a movie
        :param search_string: string to be searched
        :return:
        """
        result = []
        search_string = search_string.lower()
        for el in self._movielist:
            if search_string in el.title.lower() or search_string in el.description.lower() or search_string in el.genre.lower() or search_string in str(el.movie_id).lower():
                result.append(el)
        return result

    def get_movie_by_id(self, id: int):
        """
        Function that returns a movie by id
        :param id: id of the movie to be returned
        :return:
        """
        found=0
        for movie in self._movielist:

            if movie.movie_id == id:
                found = 1
                return movie
        if found==0:
            raise  NotFoundError(id)

    def already_exists_movie(self, movie: Movie):
        """
        Function that checks if a movie already exists
        :param movie: object of type Movie
        :return:
        """

        for x in self._movielist:
            if movie.movie_id == x.movie_id:
                return False
        return True

    def generate_movies(self, idd: int):
        str1 = ["The Action Movie",
                "Fantastic Romance Movie",
                "Epic Sci-Fi Movie",
                "Mysterious Thriller Movie",
                "Brilliant Comedy Movie",
                "Incredible Drama Movie",
                "Dazzling Fantasy Movie",
                "Enigmatic Mystery Movie",
                "Marvelous Horror Movie",
                "Spectacular Adventure Movie",
                "The Adventure Movie",
                "Fantastic Drama Movie",
                "Epic Comedy Movie",
                "Mysterious Sci-Fi Movie",
                "Brilliant Thriller Movie",
                "Incredible Romance Movie",
                "Dazzling Mystery Movie",
                "Enigmatic Action Movie",
                "Marvelous Fantasy Movie",
                "Spectacular Horror Movie"
            ]





        id_ = idd
        title = random.choice(str1)
        description= "description" + str(id_)
        genre= "genre" + str(id_)

        return Movie(id_, title, description, genre)

    def generate_n_movies(self, n: int):

        for i in range(1, n+1):
            new = self.generate_movies(i)
            self._movielist.append(new)


class MovieTextFileRepo(MovieRepo):
    def __init__(self, file_name):
        self._movielist=[]
        self.__file_name=file_name

        self.load()

    def load(self):
        try:
            file =open(self.__file_name, "r")
            values = file.readlines()
            for value in values:
                parsed_values = value.split("|")
                self.add_movie(Movie(int(parsed_values[0]), parsed_values[1], parsed_values[2], parsed_values[3].removesuffix("\n")))

            file.close()
        except FileNotFoundError as ve:
            self.generate_n_movies(20)
            self.save()
            pass

    def save(self):
        array=[]
        for movie in self._movielist:
             array.append(str(movie.movie_id) + "|" + str(movie.title) + "|" +  str(movie.description) + "|"+ str(movie.genre) + "\n")
        file=open(self.__file_name, "w")
        file.writelines(array)
        file.close()

    def add_movie(self, filmulet:Movie):
        super().add_movie(filmulet)
        self.save()

    def update_title(self, idm:int, name:str):
        super().update_title(idm, name)
        self.save()

    def update_description(self, idm:int, name:str):
        super().update_description(idm, name)
        self.save()
    def update_genre(self, idm:int, name:str):
        super().update_genre(idm, name)
        self.save()
    def remove(self, idm:int):
        super().remove(idm)
        self.save()

class MovieBinaryRepo(MovieRepo):
    def __init__(self, file_name: str):
        self._movielist = []
        self.__file_name = file_name

        self.load()


    def load(self):
        try:
            file = open(self.__file_name, "rb")
            self._movielist = pickle.load(file)
            file.close()

        except:
            self.generate_n_movies(20)
            self.save()
            pass



    def save(self):
        file = open(self.__file_name, "wb")
        pickle.dump(self._movielist, file)
        file.close()

    def add_movie(self, filmulet:Movie):
        super().add_movie(filmulet)
        self.save()

    def update_title(self, idm:int, name:str):
        super().update_title(idm, name)
        self.save()

    def update_description(self, idm:int, name:str):
        super().update_description(idm, name)
        self.save()
    def update_genre(self, idm:int, name:str):
        super().update_genre(idm, name)
        self.save()
    def remove(self, idm:int):
        super().remove(idm)
        self.save()