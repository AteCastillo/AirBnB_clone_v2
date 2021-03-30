#!/usr/bin/python3
"""New engine to save data"""
from os import getenv
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage():
    """Database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """to instantiate the clas"""
        username = getenv('HBNB_MYSQL_USER')
        passw = getenv('HBNB_MYSQL_PWD')
        hostname = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(username, passw,
                                              hostname, database),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
                Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if cls is None:
            objs = self.__session.query(State).all()
            objs += self.__session.query(City).all()
            objs += self.__session.query(User).all()
            objs += self.__session.query(Place).all()
            objs += self.__session.query(Review).all()
            objs += self.__session.query(Amenity).all()
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        new_dict = {}
        for obj in objs:
            key = type(obj).__name__ + "." + obj.id
            new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add object to database"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes on the current database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete object"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create tables"""
        Base.metadata.create_all(self.__engine)
        Session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(Session_factory)
        self.__session = Session()
