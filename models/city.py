#!/usr/bin/python3
"""class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """class City"""

    def __init__(self, *args, **kwargs):
        """class constructon"""
        self.state_id = kwargs.pop('state_id', "")
        self.name = kwargs.pop('name', "")
        super().__init__(*args, **kwargs)
