#!/usr/bin/python3
"""class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity"""

    def __init__(self, *args, **kwargs):
        """class constructon"""
        self.name = kwargs.pop('name', "")
        super().__init__(*args, **kwargs)
