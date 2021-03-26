#!/usr/bin/python3
"""File Storage Class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """FileStorage class documentation"""
    __file_path = "file.json"
    # a dictionary that contains a key with the name
    # of the class.id and value is a pointer to objects:
    __objects = {}  # save all instances of all objects, a pointer to an object
    # receives text format, converts it into dicts
    # json file will contain objects/instances based on the dict __objects
    # ex: City, and this will contain atributes
    # of the instance ex: id, created_at, etc

    def __init__(self):
        pass

    def all(self):
        """returns the dictionary __objects"""
        # like a getter of objects, to access this private dict
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key ex: User.id"""
        # id value in the dict
        key = obj.__class__.__name__ + "." + obj.__dict__["id"]
        # after creating an object, calls new from BaseModel
        # takes the instance and put inside the __objects dictionary
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dict_obj = {}
        # saves and converts every object/dictionaries into string
        for key, val in FileStorage.__objects.items():
            # the value of the key has a pointer to the object
            # same key with value from to_dict method:
            dict_obj[key] = val.to_dict()  # it has all data from the object
        with open(FileStorage.__file_path, mode="w") as f:
            f.write(json.dumps(dict_obj, indent=2))

    def reload(self):
        '''
        Method to deserializes a JSON file to an attribute __objects
        '''
        # this is the first thing that happens
        # reads a file that has a string, convert it into a dict/object
        # the dictionary objects has dicts inside
        # dict to compare:
        classes = {'BaseModel': BaseModel, 'User': User,
                   'State': State, 'City': City, 'Amenity': Amenity,
                   'Place': Place, 'Review': Review}
        f = FileStorage.__objects
        try:
            # opening file.json
            with open('{}'.format(FileStorage.__file_path), 'r') as File:
                # file.json converted to a dict "elems" that has dictionaries:
                elems = json.load(File)
                # the value of the key is a dictionary
                for key in elems:
                    # converts the key in an instance and send to __objects
                    # to every key in elems add an instance
                    # with the same key in f:
                    f[key] = classes[elems[key]['__class__']](**elems[key])
                    # for review:
                # elems[key] = Review.9324398432
                # elems[key]['__class__'] = "Review"
                # classes["Review"](**elems[User.9324398432])
                # adds to __objects[key] an instance wich
                # is an object from kwargs:
                # ** converts one dict "elems[key]" in kwargs:
                # __objects[key] = Review(**elems[Review.9324398432])
                # Review(**elems[Review.9324398432])
        except:
            pass
