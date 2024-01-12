#!/usr/bin/python3
"""Py script to list all objects and their corresponding children"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for cit in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(cit.id, cit.name, cit.state.name))
    session.close()
    engine.dispose()
