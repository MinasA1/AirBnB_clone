#!/usr/bin/python3
"""class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User"""

    def __init__(self, *args, **kwargs):
        """class constructon"""
        self.email = kwargs.pop('email', "")
        self.password = kwargs.pop('password', "")
        self.first_name = kwargs.pop('first_name', "")
        self.last_name = kwargs.pop('last_name', "")
        super().__init__(*args, **kwargs)
