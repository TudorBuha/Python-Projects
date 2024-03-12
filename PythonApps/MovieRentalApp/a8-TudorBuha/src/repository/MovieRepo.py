from src.domain.Movie import *
from random import randint, choice
from src.repository.ClientRepo import NotUniqueClientIdError, NotFoundID

class MovieRepo:
    def __init__(self):
        self._movie_list = []

    def generate(self):
        """
        Generates 20 random movies
        :return:
        """
        title_list = ["Clover field", "Clown", "The Clowns", "ClownTown", "Club Paradise", "Clue", "Cobra Verde", "Harry Potter", "Home alone", "Karate kid", "Lion king", "Cinderella", "The Godfather", "The Godfather: Part II", "The Godfather: Part III", "The Good, the Bad and the Ugly", "Good Bye, Lenin!", "Good Morning", "Vietnam", "Good Will Hunting", "Goodfellas", "The Goonies", "The Graduate", "Gran Torino", "The Grand Budapest Hotel", "The Great Dictator", "The Great Escape", "The Great Gatsby", "The Green Mile", "Groundhog Day", "Guardians of the Galaxy", "Hachi: A Dog's Tale", "Hacksaw Ridge"]
        description_list = ["A very good movie", "A very bad movie", "A very long movie", "A very short movie", "A very funny movie", "A very sad movie", "A very happy movie", "A very boring movie", "A very interesting movie", "A very scary movie"]
        genre_list = ["Action", "Adventure", "Comedy", "Crime", "Drama", "Fantasy", "Historical", "Historical fiction", "Horror", "Magical realism", "Mystery", "Paranoid Fiction", "Philosophical", "Political", "Romance", "Saga", "Satire", "Science fiction", "Social", "Speculative", "Thriller", "Urban", "Western"]
        for i in range(1,21):
            movies_id = i
            movies_title = choice(title_list)
            movies_description = choice(description_list)
            movies_genre = choice(genre_list)
            movie = Movie(movies_id, movies_title, movies_description, movies_genre)
            self._movie_list.append(movie)

    def add_movie(self, movie):
        if self.already_exists_movie(movie) is False:
            raise NotUniqueClientIdError(movie.movie_id)
        self._movie_list.append(movie)

    def display_movies(self):
        return self._movie_list

    def update_title(self, new_title, movie_id):
        found = False
        for movie in self._movie_list:
            if int(movie_id) == int(movie.movie_id):
                movie.title = str(new_title)
                found = True
                break
        if found == False:
            raise NotFoundID(movie_id)

    def update_description(self, new_description, movie_id):
        found = False
        for movie in self._movie_list:
            if int(movie_id) == int(movie.movie_id):
                movie.description= str(new_description)
                found = True
                break
        if found == False:
            raise NotFoundID(movie_id)

    def update_genre(self, new_genre, movie_id):
        found = False
        for movie in self._movie_list:
            if int(movie_id) == int(movie.movie_id):
                movie.genre = str(new_genre)
                found = True
                break
        if found == False:
            raise NotFoundID(movie_id)

    def remove(self, movie_id):
        for movie in self._movie_list:
            if int(movie_id) == int(movie.movie_id):
                self._movie_list.remove(movie)

    def search_by_title(self, title_search):
        movies_title_list = []
        for movie in self._movie_list:
            copy_title = movie.title
            if title_search.lower() in copy_title.lower():
                movies_title_list.append(movie)
        return movies_title_list

    def search_by_description(self, description_search):
        movies_description_list = []
        for movie in self._movie_list:
            copy_description = movie.description
            if description_search.lower() in copy_description.lower():
                movies_description_list.append(movie)
        return movies_description_list

    def search_by_genre(self, genre_search):
        movies_genre_list = []
        for movie in self._movie_list:
            copy_genre = movie.genre
            if genre_search.lower() in copy_genre.lower():
                movies_genre_list.append(movie)
        return movies_genre_list

    def get_movie_by_id(self, id_find):
        for movie in self._movie_list:
            if int(movie.movie_id) == int(id_find):
                return movie

    def already_exists_movie(self, movie_to_search_for):
        for current_movie in self._movie_list:
            if current_movie.movie_id == movie_to_search_for.movie_id:
                return False
        return True



