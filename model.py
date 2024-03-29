"""Models and database functions for cars db."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey

# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM
class Human(db.Model):
    """Human model."""

    __tablename__ = "humans"
    human_id = db.Column(db.Integer, primary_key=True, nullable=False)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    animals = db.relationship('Animal', backref='humans', lazy=True)


class Animal(db.Model):
    """Animal model."""

    __tablename__ = "animals"
    animal_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(db.String(50), nullable=False)
    human_id = db.Column(db.Integer, db.ForeignKey('humans.human_id'))
    animal_species = db.Column(db.String(25), nullable=False)


# End Part 1


##############################################################################
# Helper functions

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app.
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print("Connected to DB.")


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vbyobeqmycypci:d1eb2c04ccd37fb39870ca89fcd69f9608f41489da3f6df9161ac493dd71aa81@ec2-34-192-83-52.compute-1.amazonaws.com:5432/d5362spol15om4'  # YOUR URI GOES HERE
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    init_app()
