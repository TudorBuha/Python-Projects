import unittest

from src.domain.Movie import Movie
from src.repository.ClientRepo import NotFoundError
from src.repository.MovieRepo import NotUniqueMovieIdError, MovieRepo, MovieTextFileRepo, MovieBinaryRepo


class TestMovieRepo(unittest.TestCase):

    def setUp(self):
        self.movie_repo = MovieRepo()
        self.movie_repo2 = MovieTextFileRepo("movieteststext.txt")
        self.movie_repo3 = MovieBinaryRepo("moviebinary.bin")

    def test_add_movie(self):
        # Test adding a new movie
        movie = Movie(len(self.movie_repo.get_all_movies()) + 1, title="The Great Movie", description="A fantastic movie", genre="Action")
        self.movie_repo.add_movie(movie)
        self.assertIn(movie, self.movie_repo.get_all_movies())
        self.movie_repo.remove(movie.movie_id)


    def test_add_movie2(self):
        # Test adding a new movie
        movie = Movie(len(self.movie_repo2.get_all_movies()) + 1, title="The Great Movie", description="A fantastic movie", genre="Action")
        self.movie_repo2.add_movie(movie)
        self.assertIn(movie, self.movie_repo2.get_all_movies())
        self.movie_repo2.remove(movie.movie_id)

    def test_add_movie3(self):
        # Test adding a new movie
        movie = Movie(len(self.movie_repo3.get_all_movies()) + 1, title="The Great Movie", description="A fantastic movie", genre="Action")
        self.movie_repo3.add_movie(movie)
        self.assertIn(movie, self.movie_repo3.get_all_movies())
        self.movie_repo3.remove(movie.movie_id)




    def test_get_all_movies(self):

        array = []
        for el in self.movie_repo.get_all_movies():
            array.append(el)

        # Test getting all movies after adding some movies
        movies = [
            Movie(453, title="Movie 1", description="Description 1", genre="Action"),
            Movie(454, title="Movie 2", description="Description 2", genre="Drama"),
            Movie(455, title="Movie 3", description="Description 3", genre="Comedy")
        ]
        for movie in movies:
            self.movie_repo.add_movie(movie)
        self.assertEqual(self.movie_repo.get_all_movies(), array + movies)

        self.movie_repo.remove(453)
        self.movie_repo.remove(454)
        self.movie_repo.remove(455)



    def test_get_all_movies2(self):
        array = []
        for el in self.movie_repo2.get_all_movies():
            array.append(el)

        # Test getting all movies after adding some movies
        movies = [
            Movie(movie_id=401, title="Movie 1", description="Description 1", genre="Action"),
            Movie(movie_id=402, title="Movie 2", description="Description 2", genre="Drama"),
            Movie(movie_id=403, title="Movie 3", description="Description 3", genre="Comedy")
        ]
        for movie in movies:
            self.movie_repo2.add_movie(movie)
        self.assertEqual(self.movie_repo2.get_all_movies(), array + movies)
        self.movie_repo2.remove(401)
        self.movie_repo2.remove(402)
        self.movie_repo2.remove(403)

    def test_get_all_movies3(self):
        array = []
        for el in self.movie_repo3.get_all_movies():
            array.append(el)

        # Test getting all movies after adding some movies
        movies = [
            Movie(movie_id=301, title="Movie 1", description="Description 1", genre="Action"),
            Movie(movie_id=302, title="Movie 2", description="Description 2", genre="Drama"),
            Movie(movie_id=303, title="Movie 3", description="Description 3", genre="Comedy")
        ]
        for movie in movies:
            self.movie_repo3.add_movie(movie)
        self.assertEqual(self.movie_repo3.get_all_movies(), array + movies)
        self.movie_repo3.remove(301)
        self.movie_repo3.remove(302)
        self.movie_repo3.remove(303)

    def test_update_title(self):

        movie = Movie(len(self.movie_repo.get_all_movies())+1, title="The Great Movie", description="A fantastic movie", genre="Action")
        self.movie_repo.add_movie(movie)
        new_title = "Updated Title"
        self.movie_repo.update_title(movie.movie_id, new_title)
        self.assertEqual(movie.title, new_title)
    def test_update_title2(self):
        # Test updating the title of an existing movie
        movie = Movie(505, title="The Great Movie", description="A fantastic movie", genre="Action")
        self.movie_repo2.add_movie(movie)
        new_title = "Updated Title"
        self.movie_repo2.update_title(movie.movie_id, new_title)
        self.assertEqual(movie.title, new_title)
        initial_name = "John Doe"
        self.movie_repo2.update_title(movie.movie_id, initial_name)
        self.movie_repo2.remove(505)

    def test_update_title3(self):
        # Test updating the title of an existing movie
        movie = Movie(len(self.movie_repo3.get_all_movies())+1, title="The Great Movie", description="A fantastic movie", genre="Action")
        self.movie_repo3.add_movie(movie)
        new_title = "Updated Title"
        self.movie_repo3.update_title(movie.movie_id, new_title)
        self.assertEqual(movie.title, new_title)


    def test_update_description(self):
        # Test updating the description of an existing movie
        movie = Movie(1000, title="The Great Movie", description="A fantastic movie", genre="Action")
        self.movie_repo.add_movie(movie)
        new_description = "Updated Description"
        self.movie_repo.update_description(movie.movie_id, new_description)
        self.assertEqual(movie.description, new_description)


    def test_update_description2(self):
        # Test updating the description of an existing movie
        movie = Movie(987, title="The Great Movie", description="A fantastic movie", genre="Action")
        self.movie_repo2.add_movie(movie)
        new_description = "Updated Description"
        self.movie_repo2.update_description(movie.movie_id, new_description)
        self.assertEqual(movie.description, new_description)
        self.movie_repo2.remove(987)


    def test_update_description3(self):

        movie = Movie(len(self.movie_repo3.get_all_movies()) + 1, title="The Great Movie", description="A fantastic movie", genre="Action")
        self.movie_repo3.add_movie(movie)
        new_description = "Updated Description"
        self.movie_repo3.update_description(movie.movie_id, new_description)
        self.assertEqual(movie.description, new_description)


    def test_update_genre(self):
        # Test updating the genre of an existing movie
        movie = Movie(len(self.movie_repo.get_all_movies()) + 1, title="The Great Movie", description="A fantastic movie", genre="Action")
        self.movie_repo.add_movie(movie)
        new_genre = "Updated Genre"
        self.movie_repo.update_genre(movie.movie_id, new_genre)
        self.assertEqual(movie.genre, new_genre)

    def test_update_genre2(self):

        movie = Movie(len(self.movie_repo2.get_all_movies()) + 1, title="The Great Movie", description="A fantastic movie", genre="Action")
        self.movie_repo2.add_movie(movie)
        new_genre = "Updated Genre"
        self.movie_repo2.update_genre(movie.movie_id, new_genre)
        self.assertEqual(movie.genre, new_genre)
        initial_name="Action"
        self.movie_repo2.update_genre(movie.movie_id,initial_name)
    def test_update_genre3(self):
        # Test updating the genre of an existing movie
        movie = Movie(len(self.movie_repo3.get_all_movies()) + 1, title="The Great Movie", description="A fantastic movie", genre="Action")
        self.movie_repo3.add_movie(movie)
        new_genre = "Updated Genre"
        self.movie_repo3.update_genre(movie.movie_id, new_genre)
        self.assertEqual(movie.genre, new_genre)
        initial_name="Action"
        self.movie_repo3.update_genre(movie.movie_id, initial_name)

    def test_remove(self):
        # Test removing an existing movie
        movie = Movie(len(self.movie_repo.get_all_movies()) + 1, title="The Great Movie", description="A fantastic movie", genre="Action")
        self.movie_repo.add_movie(movie)
        self.movie_repo.remove(movie.movie_id)
        self.assertNotIn(movie, self.movie_repo.get_all_movies())


    def test_remove2(self):
        # Test removing an existing movie
        movie = Movie(len(self.movie_repo2.get_all_movies()) + 1, title="The Great Movie", description="A fantastic movie", genre="Action")
        self.movie_repo2.add_movie(movie)
        self.movie_repo2.remove(movie.movie_id)
        self.assertNotIn(movie, self.movie_repo2.get_all_movies())

    def test_remove3(self):
        # Test removing an existing movie
        movie = Movie(len(self.movie_repo3.get_all_movies()) + 1, title="The Great Movie", description="A fantastic movie", genre="Action")
        self.movie_repo3.add_movie(movie)
        self.movie_repo3.remove(movie.movie_id)
        self.assertNotIn(movie, self.movie_repo3.get_all_movies())


if __name__ == '__main__':
    unittest.main()