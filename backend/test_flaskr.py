import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from src.api import create_app
from src.database.models import db_drop_and_create_all, Actors

load_dotenv()

database_username = os.environ['DB_USER']
database_password = os.environ['DB_PASSWORD']
db_host = os.environ['DB_HOST']
db_port = os.environ['DB_PORT']
database_name = os.environ['DB_NAME']
casting_assistant_token = os.environ['CASTING_ASSISTANT_TOKEN']
casting_director_token = os.environ['CASTING_DIRECTOR_TOKEN']
executive_producer_token = os.environ['EXECUTIVE_PRODUCER_TOKEN']

database_path = 'postgresql://{}:{}@{}:{}/{}'.format(
    database_username,
    database_password,
    db_host,
    db_port,
    database_name
)

class TriviaTestCase(unittest.TestCase):
    """This class represents the test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.database_name = "casting_agency_test"
        self.database_path = database_path
        
        self.app = create_app({
            "SQLALCHEMY_DATABASE_URI": self.database_path
        })

        self.client = self.app.test_client
        db_drop_and_create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def getHeaders(self, token=''):
        return {'authorization': "Bearer " + token}
    
    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """


    ####
    # Testing for Actors
    ####

    def test_get_actors(self):
        headers = self.getHeaders(casting_assistant_token) 
        res = self.client().get("/actors", headers=headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertTrue(len(data["actors"]))

    def test_get_actors_without_token(self):
        res = self.client().get("/actors")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "Authorization header is expected.")

    def test_get_actors_failure(self):
        headers = self.getHeaders(casting_assistant_token)
        res = self.client().get("/actor",headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "resource not found")

    def test_delete_actors_unauthorized(self):
        headers = self.getHeaders(casting_assistant_token)
        res = self.client().delete("/actors/1", headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data["success"])

    def test_delete_actors(self):
        headers = self.getHeaders(casting_director_token)
        res = self.client().delete("/actors/1", headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["delete"], 1)
    
    def test_delete_actors_not_found(self):
        headers = self.getHeaders(casting_director_token)
        res = self.client().delete("/actors/200", headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def test_create_new_actors(self):
        headers = self.getHeaders(casting_director_token)
        res = self.client().post("/actors", json={
            "name": "New actor",
            "age": 1993,
            "gender": "Male"
        }, headers=headers )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertTrue(len(data["actors"]))

    def test_create_new_actors_failure(self):
        headers = self.getHeaders(casting_director_token)
        res = self.client().post("/actors", json={
            "name": "New actor",
            "age": 1993
        }, headers=headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def test_update_actors(self):
        headers = self.getHeaders(casting_director_token)
        res = self.client().patch("/actors/1", json={
            "name": "New actor",
            "age": 1993,
            "gender": "Male"
        }, headers=headers )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertTrue(len(data["actors"]))
    
    ####
    # Testing for Movies
    ####
    def test_get_movies(self):
        headers = self.getHeaders(casting_assistant_token)
        res = self.client().get("/movies", headers=headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertTrue(len(data["movies"]))

    def test_get_movies_without_token(self):
        res = self.client().get("/movies")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "Authorization header is expected.")

    def test_get_movies_failure(self):
        headers = self.getHeaders(casting_assistant_token)
        res = self.client().get("/movie",headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "resource not found")

    def test_delete_movies_unauthorized(self):
        headers = self.getHeaders(casting_assistant_token)
        res = self.client().delete("/movies/1", headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data["success"])

    def test_delete_movies(self):
        headers = self.getHeaders(executive_producer_token)
        res = self.client().delete("/movies/1", headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["delete"], 1)
    
    def test_delete_movies_not_found(self):
        headers = self.getHeaders(executive_producer_token)
        res = self.client().delete("/movies/200", headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def test_create_new_movies(self):
        headers = self.getHeaders(executive_producer_token)
        res = self.client().post("/movies", json={
            "title": "New Movies",
            "release_date": "2024-8-10"
        }, headers=headers )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertTrue(len(data["movies"]))

    def test_create_new_movies_failure(self):
        headers = self.getHeaders(executive_producer_token)
        res = self.client().post("/movies", json={
            "title": "New Movies"
        }, headers=headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def test_update_movies(self):
        headers = self.getHeaders(executive_producer_token)
        res = self.client().patch("/movies/1", json={
            "title": "Update Movies",
            "release_date": "2024-8-10"
        }, headers=headers )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertTrue(len(data["movies"]))

    def test_create_movies_unauthorized(self):
        headers = self.getHeaders(casting_director_token)
        res = self.client().delete("/movies/1", headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data["success"])

    def test_get_url_notfound(self):
        res = self.client().get("/test-url")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "resource not found")
    
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()