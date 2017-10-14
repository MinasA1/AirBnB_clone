#!/usr/bin/python3
"""class Place"""

from models.base_model import BaseModel


class Place(BaseModel):
    """class Place"""
    def __init__(self, *args, **kwargs):
        """class constructor"""
        self.city_id = kwargs.pop('city_id', "")
        self.user_id = kwargs.pop('user_id', "")
        self.name = kwargs.pop('name', "")
        self.description = kwargs.pop('description', "")
        self.number_rooms = int(kwargs.pop('number_rooms', 0))
        self.number_bathrooms = int(kwargs.pop('number_bathrooms', 0))
        self.max_guest = int(kwargs.pop('max_guest', 0))
        self.price_by_night = int(kwargs.pop('price_by_night', 0))
        self.latitude = float(kwargs.pop('latitude', 0.0))
        self.longitude = float(kwargs.pop('longitude', 0.0))
        self.amenity_ids = list(kwargs.pop('amenity_id', []))
        super().__init__(*args, **kwargs)
