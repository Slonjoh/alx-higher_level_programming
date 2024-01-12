#!/usr/bin/python3
"""Py script to list all state.ids that match with state entered"""
from sys import argv
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    flag = 0
    instr = func.binary(argv[4])
    for instance in session.query(State)\
                           .filter(State.name == instr).order_by(State.id):
        print('{}'.format(instance.id))
        flag = 1
    if not flag:
        print("Not found")
    session.close()
    engine.dispose()
