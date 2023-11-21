#!/usr/bin/python3
"""New engine DBStorage"""
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.state import State
from models.review import Review
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.base_model import Base

class DBStorage:
    """
    Private class attribute
    SQLalchemy database
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        create the engine,
        the engine must be linked to the MySQL database and
        user created before (hbnb_dev and hbnb_dev_db)
        """

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                        format(getenv("HBNB_MYSQL_USER"),
                                            getenv("HBNB_MYSQL_PWD"),
                                            getenv("HBNB_MYSQL_HOST"),
                                            getenv("HBNB_MYSQL_DB")),
                                        pool_pre_ping=True)
        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns dictionary with objects
        """
        if cls:
            objs = self.__session.query(cls)
        else:
            objs = self.__session.query(State).all()
            objs += self.__session.query(City).all()
            objs += self.__session.query(User).all()
            objs += self.__session.query(Place).all()
            objs += self.__session.query(Amenity).all()
            objs += self.__session.query(Review).all()

        dic = {}
        for obj in objs:
            keyz = '{}.{}'.format(type(obj).__name__, obj.id)
            dic[keyz] = obj
        return dic

    def new(self, obj):
        """
        add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """commit all changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the curren db session obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database (feature of SQLAlchemy)
        (WARNING: all classes who inherit from Base must be imported before calling
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session

    def close(self):
        """
        calls close() or remove()
        """
        self.__session.close()
