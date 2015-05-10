from magic_reservation_system import MagicReservationSystem
import sqlite3

class PrettyData:

    def __init__(self):
        self.reservetaion_system = MagicReservationSystem()
        self.db = sqlite3.connect("cinema.db")
        self.cursor = self.db.cursor()

    def print_show_movies(self):
        print("Current movies: ")
        for movies in self.reservetaion_system.show_movies():
            print("[{}]".format(movies[0]), movies[1], "({})".format(movies[2]))

    def print_show_movie_projections(self, movie_id):
        movie_name = self.cursor.execute("SELECT movie_name FROM Movies WHERE movie_id = ?", (movie_id,))
        name = ""
        for m in movie_name:
            name = m[0]
        print("Projections for movie '%s': " % name)
        for projections in self.reservetaion_system.show_movie_projections(movie_id):
            print("[{}]".format(projections[0]), projections[1], projections[2], "({})".format(projections[3]))

    def print_show_movie_projections(self, movie_id):
        movie_name = self.cursor.execute("SELECT movie_name FROM Movies WHERE movie_id = ?", (movie_id,))
        name = ""
        for m in movie_name:
            name = m[0]
        print("Projections for movie '%s': " % name)
        for projections in self.reservetaion_system.show_movie_projections(movie_id):
            print("[{}]".format(projections[0]), projections[1], projections[2], "({})".format(projections[3]))

    def print_show_movie_projections_with_date(self, movie_id, movie_date):
        movie_name = self.cursor.execute("SELECT Movies.movie_name, Projections.movie_date FROM Movies JOIN Projections WHERE Movies.movie_id = ?, Projections.movie_date = ? ", (movie_id, movie_date,))
        m_name = ""
        m_date = ""
        for m in movie_name:
            print(m)
        #print("Projections for movie '%s': " % name)
        #for projections in self.reservetaion_system.show_movie_projections(movie_id):
         #   print("[{}]".format(projections[0]), projections[1], projections[2], "({})".format(projections[3]))


p = PrettyData()
#p.print_show_movies()
#p.print_show_movie_projections(1)
p.print_show_movie_projections_with_date(4, "2015-05-04")
