#!/usr/bin/python3
"""class Filestorage"""
import json


class FileStorage:
    """class FileStorage"""
    __file_path = "file.json"
    __objects = {}
    __count = {'BaseModel': 0, 'User': 0, 'State': 0,
               'City': 0, 'Amenity': 0, 'Place': 0,
               'Review': 0}

    def count(self):
        """return objcount"""
        return self.__count

    def all(self):
        """
        all - returns the dictionary __objects
        Args:
            None
        Return:
            None
        """
        return self.__objects

    def new(self, obj):
        """
        new - sets in __objects the obj given
        Args:
            obj(unk) - object to copy into __objects dictionary
        Return:
            None
        """
        self.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """
        save - serializes __objects to JSON file
        Args:
            None
        Return:
            None
        """
        js = {}
        for k in self.__objects:
            js[k] = self.__objects[k].to_dict()
        js = json.dumps(js)
        with open(self.__file_path, "w") as jsf:
            jsf.write(js)

    def reload(self):
        """
        reload - deserializes JSON file back to __objects
        Arg:
            None
        Return:
            None
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        classesD = {'BaseModel': BaseModel, 'User': User, 'State': State,
                    'City': City, 'Amenity': Amenity, 'Place': Place,
                    'Review': Review}
        try:
            with open(self.__file_path, "r") as jsf:
                js = jsf.read()
            js = json.loads(js)
            for key in js:
                name = key.split(".")[0]
                if name in classesD:
                    self.__objects[key] = classesD[name](**js[key])
                    self.__count[name] += 1
        except:
            return
