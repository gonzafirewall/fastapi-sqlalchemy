import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
SQLALCHEMY_DATABASE_URL = "sqlite:///database.sqlite"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Session = sessionmaker(bind=engine)

Base = declarative_base()