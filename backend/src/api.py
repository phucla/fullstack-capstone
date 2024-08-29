import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Actors, Movies, db
from .auth.auth import AuthError, requires_auth

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        setup_db(app)
    else:
        database_path = test_config.get('SQLALCHEMY_DATABASE_URI')
        setup_db(app, database_path=database_path)

    """
    Set up CORS. Allow '*' for origins. Delete the sample route after completing the DONEs
    """
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    """
    Use the after_request decorator to set Access-Control-Allow
    """
    @app.after_request
    def after_request(response):
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
      response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
      return response

    '''
    @DONE uncomment the following line to initialize the datbase
    !! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
    !! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
    !! Running this funciton will add one
    '''
    db_drop_and_create_all()
    define_routers(app)
    error_handling(app)
    return app

# ROUTES
def define_routers(app):
    '''
    @DONE implement endpoint
        GET /actors
            it should be a public endpoint
            it should contain only the actors.short() data representation
        returns status code 200 and json {"success": True, "actors": actors} where actors is the list of actors
            or appropriate status code indicating reason for failure
    '''
    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        try:
            actors = Actors.query.order_by(Actors.id).all()

            if len(actors) == 0:
                    abort(404)

            actors_short = [actor.short() for actor in actors]
            return jsonify({
                'success': True,
                'actors': actors_short
            })
        except Exception as e:
            print(f"An error occurred: {e}")
            abort(422)
            
    '''
    @DONE implement endpoint
        GET /actors-detail
            it should require the 'get:actors-detail' permission
            it should contain the actor.short() data representation
        returns status code 200 and json {"success": True, "actors": actors} where actors is the list of actors
            or appropriate status code indicating reason for failure
    '''
    @app.route('/actors-detail', methods=['GET'])
    @requires_auth('get:actors-detail')
    def get_actors_detail(payload):
        try:
            actors = Actors.query.order_by(Actors.id).all()

            if len(actors) == 0:
                    abort(404)

            actors_details = [actor.short() for actor in actors]
            return jsonify({
                'success': True,
                'actors': actors_details
            })
        except Exception as e:
            print(f"An error occurred: {e}")
            abort(422)

    '''
    @DONE implement endpoint
        POST /actors
            it should create a new row in the actors table
            it should require the 'post:actors' permission
            it should contain the actor.short() data representation
        returns status code 200 and json {"success": True, "actors": actor} where actor an array containing only the newly created actor
            or appropriate status code indicating reason for failure
    '''
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor(payload):
        try:
            data = request.get_json()
            if ("name" not in data
            or "age" not in data
            or "gender" not in data):
                abort(422)

            actor = Actors(
                name = data["name"],
                age = data["age"],
                gender = data["gender"]
            )
            actor.insert()

            return jsonify({
                'success': True,
                'actors': [actor.short()]
            })
        except Exception as e:
            print(f"An error occurred: {e}")
            abort(422)

    '''
    @DONE implement endpoint
        PATCH /actors/<id>
            where <id> is the existing model id
            it should respond with a 404 error if <id> is not found
            it should update the corresponding row for <id>
            it should require the 'patch:actors' permission
        returns status code 200 and json {"success": True, "actors": actor} where actor an array containing only the updated actor
            or appropriate status code indicating reason for failure
    '''
    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(payload, id):
        try:
            data = request.get_json()
            name = data.get('name', None)
            age = data.get('age', None)
            gender = data.get('gender', None)

            actor = Actors.query.filter_by(id=id).one_or_none()
            if actor is None:
                abort(404)

            if name:
                actor.name = name
            if age:
                actor.age = age
            if gender:
                actor.gender = gender
            actor.update()

            return jsonify({
                'success': True,
                'actors': [actor.short()]
            })
        except Exception as e:
            print(f"An error occurred: {e}")
            abort(422)

    '''
    @DONE implement endpoint
        DELETE /actors/<id>
            where <id> is the existing model id
            it should respond with a 404 error if <id> is not found
            it should delete the corresponding row for <id>
            it should require the 'delete:actors' permission
        returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
            or appropriate status code indicating reason for failure
    '''
    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, id):
        try:
            actor = Actors.query.filter(Actors.id == id).one_or_none()
            if actor is None:
                abort(404)

            actor.delete()

            return jsonify({
                'success': True,
                'delete': id
            })
        except Exception as e:
            print(f"An error occurred: {e}")
            abort(422)


    '''
    @DONE implement endpoint
        GET /movies
            it should be a public endpoint
            it should contain only the movies.short() data representation
        returns status code 200 and json {"success": True, "movies": movies} where movies is the list of movies
            or appropriate status code indicating reason for failure
    '''
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
        try:
            movies = Movies.query.order_by(Movies.id).all()

            if len(movies) == 0:
                    abort(404)

            movies_short = [movie.short() for movie in movies]
            return jsonify({
                'success': True,
                'movies': movies_short
            })
        except Exception as e:
            print(f"An error occurred: {e}")
            abort(422)
            
    '''
    @DONE implement endpoint
        GET /movies-detail
            it should require the 'get:movies-detail' permission
            it should contain the movie.short() data representation
        returns status code 200 and json {"success": True, "movies": movies} where movies is the list of movies
            or appropriate status code indicating reason for failure
    '''
    @app.route('/movies-detail', methods=['GET'])
    @requires_auth('get:movies-detail')
    def get_movies_detail(payload):
        try:
            movies = Movies.query.order_by(Movies.id).all()

            if len(movies) == 0:
                    abort(404)

            movies_details = [movie.short() for movie in movies]
            return jsonify({
                'success': True,
                'movies': movies_details
            })
        except Exception as e:
            print(f"An error occurred: {e}")
            abort(422)

    '''
    @DONE implement endpoint
        POST /movies
            it should create a new row in the movies table
            it should require the 'post:movies' permission
            it should contain the movie.short() data representation
        returns status code 200 and json {"success": True, "movies": movie} where movie an array containing only the newly created movie
            or appropriate status code indicating reason for failure
    '''
    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(payload):
        try:
            data = request.get_json()
            if ("title" not in data
            or "release_date" not in data):
                abort(422)

            movie = Movies(
                title = data["title"],
                release_date = data["release_date"]
            )
            movie.insert()

            return jsonify({
                'success': True,
                'movies': [movie.short()]
            })
        except Exception as e:
            print(f"An error occurred: {e}")
            abort(422)

    '''
    @DONE implement endpoint
        PATCH /movies/<id>
            where <id> is the existing model id
            it should respond with a 404 error if <id> is not found
            it should update the corresponding row for <id>
            it should require the 'patch:movies' permission
        returns status code 200 and json {"success": True, "movies": movie} where movie an array containing only the updated movie
            or appropriate status code indicating reason for failure
    '''
    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(payload, id):
        try:
            data = request.get_json()
            title = data.get('title', None)
            release_date = data.get('release_date', None)

            movie = Movies.query.filter_by(id=id).one_or_none()
            if movie is None:
                abort(404)

            if title:
                movie.title = title
            if release_date:
                movie.release_date = release_date
            movie.update()

            return jsonify({
                'success': True,
                'movies': [movie.short()]
            })
        except Exception as e:
            print(f"An error occurred: {e}")
            abort(422)

    '''
    @DONE implement endpoint
        DELETE /movies/<id>
            where <id> is the existing model id
            it should respond with a 404 error if <id> is not found
            it should delete the corresponding row for <id>
            it should require the 'delete:movies' permission
        returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
            or appropriate status code indicating reason for failure
    '''
    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, id):
        try:
            movie = Movies.query.filter(Movies.id == id).one_or_none()
            if movie is None:
                abort(404)

            movie.delete()

            return jsonify({
                'success': True,
                'delete': id
            })
        except Exception as e:
            print(f"An error occurred: {e}")
            abort(422)

# Error Handling
def error_handling(app):
    '''
    Example error handling for unprocessable entity
    '''


    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422


    '''
    @DONE implement error handlers using the @app.errorhandler(error) decorator
        each error handler should return (with approprate messages):
                jsonify({
                        "success": False,
                        "error": 404,
                        "message": "resource not found"
                        }), 404

    '''
    @app.errorhandler(404)
    def not_found_request(error):
        return jsonify({
            "success": False,
            "message": "resource not found",
            "error": 404,
        }), 404


    '''
    @DONE implement error handler for AuthError
        error handler should conform to general task above
    '''
    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            'success': False,
            'error': error.error['code'],
            'message': error.error['description'],
        }), error.status_code

app = create_app()