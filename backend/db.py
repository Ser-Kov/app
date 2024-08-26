from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///taskmanager.db', echo=True)

Base = declarative_base()



