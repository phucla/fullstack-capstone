import os
from sqlalchemy import Column, String, Integer, Date, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from dotenv import load_dotenv
load_dotenv()

database_username = os.environ['DB_USER']
database_password = os.environ['DB_PASSWORD']
db_host = os.environ['DB_HOST']
db_port = os.environ['DB_PORT']
database_name = os.environ['DB_NAME']

database_path = 'postgresql://{}:{}@{}:{}/{}'.format(
    database_username,
    database_password,
    db_host,
    db_port,
    database_name
)

db = SQLAlchemy()

"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
    # add one demo row which is helping in POSTMAN test
    actors = Actors(
        name='Join',
        age=1993,
        gender='Male'
    )
    actors.insert()

    movies = Movies(
        title='Spider Man',
        release_date='2024-8-10'
    )
    movies.insert()
    
# ROUTES

'''
Actors
'''

class Actors(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    '''
    short()
        short form representation of the Actors model
    '''

    def short(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }

    '''
    insert()
        inserts a new model into a database
        EXAMPLE
            actors = Actors(name=req_name, age=req_age, gender=req_gender)
            actors.insert()
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
        EXAMPLE
            actors = Actors(name=req_name, age=req_age, gender=req_gender)
            actors.delete()
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
        EXAMPLE
            actors = Actors.query.filter(Actors.id == id).one_or_none()
            actors.name = 'Black Bi'
            actors.update()
    '''

    def update(self):
        db.session.commit()

'''
Movies
'''

class Movies(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    '''
    short()
        short form representation of the Movies model
    '''

    def short(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }

    '''
    insert()
        inserts a new model into a database
        EXAMPLE
            movies = Movies(title=title, release_date=req_release_date)
            actors.insert()
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
        EXAMPLE
            movies = Movies(title=title, release_date=req_release_date)
            actors.delete()
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
        EXAMPLE
            movies = Movies.query.filter(Movies.id == id).one_or_none()
            movies.title = 'Supper Man'
            movies.update()
    '''

    def update(self):
        db.session.commit()