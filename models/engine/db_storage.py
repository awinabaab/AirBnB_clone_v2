#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models in a database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiates an instance of DBStorage"""
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")

        connection_str = (
                f"mysql+mysqldb://{user}:{pwd}@{host}/{db}"
                )
        self.__engine = create_engine(connection_str, pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on current database session all objects depending on class"""
        obj_dict = {}
        if cls:
            if isinstance(cls, type(Base)):
                query = self.__session.query(cls).all()
            else:
                pass
        else:
            query_objs = [User, State, City, Amenity, Place, Review]
            query = []
            for q_obj in query_objs:
                if isinstance(q_obj, type(Base)):
                    query.extend(self.__session.query(q_obj).all())
                else:
                    continue

        for obj in query:
            key = f"{obj.__class__.__name__}.{obj.id}"
            del obj._sa_instance_state
            obj_dict.update({key: obj})
        return obj_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
