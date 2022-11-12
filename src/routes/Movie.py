from flask import Blueprint, jsonify, request
from models.MovieModel import MovieModel
from models.entities.Movie import Movie
import uuid

main = Blueprint('movie_blueprint', __name__)


@main.route('/')
def get_movies():
    try:
        movies = MovieModel.get_movies()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_movie(id):
    try:
        movie = MovieModel.get_movie(id)
        if movie != None:
            return jsonify(movie)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_movie():
    try:
        id = str(uuid.uuid4())
        title = request.json['title']
        duration = int(request.json['duration'])
        released = request.json['released']
        movie = Movie(id, title, duration, released)
        result = MovieModel.add_movie(movie)
        if result == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': 'Error on insert'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/delete/<id>', methods=['DELETE'])
def delete_movie(id):
    try:
        movie = Movie(id)
        result = MovieModel.delete_movie(movie)
        if result == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': 'No movie deleted'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_movie(id):
    try:
        title = request.json['title']
        duration = int(request.json['duration'])
        released = request.json['released']
        movie = Movie(id, title, duration, released)
        result = MovieModel.update_movie(movie)
        if result == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': 'Error on updated'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500