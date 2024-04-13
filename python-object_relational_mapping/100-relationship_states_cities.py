#!/usr/bin/python3
'''Creates new state: California. with the city: “San Francisco”
 from the database hbtn_0e_100_usa
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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_city = City(name="San Francisco", state=State(name="California"))
    session.add(new_city)
    session.commit()
