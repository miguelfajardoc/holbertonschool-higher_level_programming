#!/usr/bin/python3
""" definition of state model
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    search = session.query(State).filter(State.name == argv[4]).first()
    if search:
        print(search.id)
    else:
        print("Not found")
