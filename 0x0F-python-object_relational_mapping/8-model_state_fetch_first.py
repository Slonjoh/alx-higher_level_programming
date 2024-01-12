#!/usr/bin/python3
"""Py script prints first state object"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, exc
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).first()
    if result:
        print("{}: {}".format(result.id, result.name))
    else:
        print("Nothing")
