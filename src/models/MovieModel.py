from database.db import get_connection
from .entities.Movie import Movie


class MovieModel():
    @classmethod
    def get_movies(self):
        try:
            connection = get_connection()
            movies = []

            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT id, title, duration, released FROM movie ORDER BY title ASC')
                result = cursor.fetchall()
                for row in result:
                    movie = Movie(row[0], row[1], row[2], row[3])
                    movies.append(movie.to_JSON())

            connection.close()
            return movies

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_movie(self, id):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT id, title, duration, released FROM movie WHERE id = %s', (id,))
                result = cursor.fetchone()
                movie = None
                if result != None:
                    movie = Movie(result[0], result[1], result[2], result[3])
                    movie = movie.to_JSON()

            connection.close()
            return movie

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_movie(self, movie):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute('''
                INSERT INTO movie (id, title, duration, released) VALUES (%s, %s, %s, %s)
                ''', (movie.id, movie.title, movie.duration, movie.released))
                result = cursor.rowcount
                connection.commit()

            connection.close()
            return result

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_movie(self, movie):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM movie WHERE id = %s', (movie.id,))
                result = cursor.rowcount
                connection.commit()

            connection.close()
            return result

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_movie(self, movie):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute('''
                UPDATE movie SET title = %s, duration = %s, released = %s WHERE id = %s
                ''', (movie.title, movie.duration, movie.released, movie.id))
                result = cursor.rowcount
                connection.commit()

            connection.close()
            return result

        except Exception as ex:
            raise Exception(ex)
