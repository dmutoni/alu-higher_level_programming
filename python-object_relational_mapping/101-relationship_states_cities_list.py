#!/usr/bin/python3
'''Lists all states and the cities within them
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}".format(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            pool_pre_ping=True)
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")
