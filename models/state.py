#!/usr/bin/python3
"""class state"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class State"""
    def __init__(self, *args, **kwargs):
        """class constructor"""
        self.name = kwargs.pop('name', "")
        super().__init__(*args, **kwargs)
