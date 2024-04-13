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
    for city in session.query(City).order_by(City.id).all():
        print(f"{city.id}: {city.name} -> {city.state.name}")
