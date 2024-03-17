#!/usr/bin/python3
"""Script to print all states from the database.

This script connects to a MySQL database using SQLAlchemy and retrieves
all state records from the 'states' table. It then prints the ID and
name of each state.

Usage:
    $ python3 script_name.py <username> <password> <database_name>

Args:
    username (str): The username for the MySQL database.
    password (str): The password for the MySQL database.
    database_name (str): The name of the MySQL database.

Example:
    $ python3 script_name.py root password my_database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
