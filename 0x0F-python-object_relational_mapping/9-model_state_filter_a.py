#!/usr/bin/python3
"""Py script to list all state objects that contain the letter a"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        if 'a' in instance.name:
            print('{}: {}'.format(instance.id, instance.name))
    session.close()
    engine.dispose()
