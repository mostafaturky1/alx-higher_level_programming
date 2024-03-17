#!/usr/bin/python3
"""Start link class to table in database
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)
session = session()

states = session.query(State).order_by(State.id)

for state in states:
    print("{}: {}".format(state.id, state.name))
