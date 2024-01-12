#!/usr/bin/python3
"""Py script to print all city objects from database"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for cit, sta in session.query(City, State)\
                           .join(State)\
                           .filter(State.id == City.state_id)\
                           .order_by(City.id):
        print("{}: ({}) {}".format(sta.name, cit.id, cit.name))
