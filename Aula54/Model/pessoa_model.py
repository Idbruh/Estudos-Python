import sqlalchemy as db
from sqlalchemy.ext.declarative import  declarative_base

Base = declarative_base

class Pessoa(Base):
    __tablename__