#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""

import sys
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3])
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for states in session.query(State).order_by(State.id):
        if 'a' in states.name:
            session.delete(states)
    session.commit()
    session.close()
