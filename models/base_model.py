#!/usr/bin/python3
"""
File: base_model.py
"""
import uuid
import datetime
import models
# import storage
# from datetime import datetime
# import models
# BaseModel = models.base_model.BaseModel


class BaseModel:
    """
    class BaseModel definition for AirBnB clone project
    This is the core object from which all objects are derived
    """
    def __init__(self, *args, **kwargs):
        """
        __init__ - initialze BaseModel object
        Args:
            args(tuple) - should have zero arguments (not used)
            kwargs(dict) - if variable exists, then init instance with data
                Note, datetime format is 2017-09-28 21:05:54.119572
        Return:
            None
        """
        format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
        if len(args):
            print("base_model.py: Should have zero args to __init__()")
            return
        for key in kwargs:
            if key == "id":
                self.id = kwargs.get("id")
                continue
            if key == "created_at":
                self.created_at = datetime.datetime.strptime(
                    kwargs["created_at"], format)
                continue
            if key == "updated_at":
                self.updated_at = datetime.datetime.strptime(
                    kwargs["updated_at"], format)
                continue
            if key == "__class__":
                continue
            setattr(self, key,  kwargs[key])
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """
        __str__ - print method for BaseModel instance
        Args:
            None
        Return:
            None
        """
        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        save - updates public instance attribute, updated_at, with
            current timestamp
        Args:
            None
        Return:
            None
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        to_dict - return dictionary with copy all key/value pairs of __dict__
        Args:
            None
        Return:
            entire copy of dictionary instance and must stringify some
            JSON modifications
        """
        d = self.__dict__.copy()
        d['__class__'] = self.__class__.__name__

        format = "%Y-%m-%dT%H:%M:%S.%f"
        d['created_at'] = str(self.__dict__['created_at'].strftime(format))
        d['updated_at'] = str(self.__dict__['updated_at'].strftime(format))
        return d
