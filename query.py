"""
This file is the place to write solutions for parts two and three of skills-
sqlalchemy. Remember to consult the exercise instructions for more complete
explanations of the assignment.
All classes from model.py are being imported for you here, so refer to classes
by just their class name (not model.ClassName).
"""
# from sqlalchemy.sql import *
# from sqlalchemy import Column, Integer, String, create_engine, Date
# #from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import Session
# import pandas.io.sql as sqlio
# from sqlalchemy.sql import select

# import pandas as pd
from model import *

init_app()


# -----------------
# PART TWO: QUERIES
# -----------------

# Get the human with the id 2.
q1 = "select * from humans where human_id = 2"

# Get the *first* animal with the species 'fish'

q2 = "SELECT * FROM animals where animal_species = 'fish'"

# Get all of the animals for the human with the id 5 and the animal species 'dog'
q3 = "select * from animals where human_id = 5 and animal_species = 'dog'"

# Get all the animals that were born after 2015 (do not include animals without birth years).
q4 = "select * from animals where birth_year > 2015"

# Find the humans with first names that start with 'J'
q5 = "select * from humans where fname like 'J%'"

# Find all the animals without birth years in the database.
q6 = "select * from animals where birth_year isnull"

# Find all animals that are either fish or rabbits
q7 = "select * from animals where animal_species = 'fish' or animal_species = 'rabbit'"

# Find all the humans whose email addresses do not contain 'gmail'
q8 = f"select * from humans where email not LIKE '%gmail%'"

# ---------------------
# PART THREE: FUNCTIONS
# ---------------------

# ***Do not use more than one query for each function***

# 1. Write a function, print_directory, which does not take any arguments
#    and prints out each human (once) with a list of their animals.

#    The output should look like this (with tabs to indent each animal name under
#    a human's name)

#       Human_first_name Human_last_name
#           Animal name (animal species)
#           Animal name (animal species)
#
#       Human_first_name Human_last_name
#           Animal name (animal species)

# engine = create_engine(
#     'postgresql://vbyobeqmycypci:d1eb2c04ccd37fb39870ca89fcd69f9608f41489da3f6df9161ac493dd71aa81@ec2-34-192-83-52.compute-1.amazonaws.com:5432/d5362spol15om4', echo=False)
# Base = declarative_base(bind=engine)
# Session = sessionmaker(bind=engine)
# session = Session()
# conn = session.bind


def print_directory():
    """Print a list of each human with their animals"""
    humans = Human.query.all()

    for human in humans:
        print(human.fname, human.lname)
        for animal in human.animals:
            print('\t{} ({})'.format(animal.name, animal.animal_species))
        print()


print_directory()
# 2. Write a function, get_animals_by_name, which takes in a string representing
#    an animal name (or part of an animal name) and *returns a list* of Animal
#    objects whose names contain that string.


def get_animals_by_name(name):
    """"""
    animals = Animal.query.all()
    animals_by_name = []
    for animal in animals:
        if animal.name == name:
            animals_by_name.append(animal.name)
    return f'animals that match that name are {animals_by_name}'


print(get_animals_by_name('Fluffy'))


# 3. Write a function, find_humans_by_animal_species, which takes in an animal
#    species and *returns a list* of all of Human objects who have animals of
#    that species.


def find_humans_by_animal_species(species):
    """"""
    animals = Animal.query.all()
    humans = Human.query.all()
    human_matches = []
    for animal in animals:
        if animal.animal_species == species:
            for human in humans:
                if animal.human_id == human.human_id and f'{human.fname} {human.lname}' not in human_matches:
                    human_matches.append(f'{human.fname} {human.lname}')
    return human_matches


print(find_humans_by_animal_species('cat'))
