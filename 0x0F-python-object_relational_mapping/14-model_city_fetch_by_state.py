#!/usr/bin/python3
""" cities and states with alchemy
"""

from sqlalchemy import asc
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    sesion = session.query(City, State).join(State).order_by(asc(City.id)).all()
    for cities, states in sesion:
        print("{}: ({:d}) {}".format(states.name, cities.id, cities.name))
