#!/usr/bin/python3
"""class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review"""

    def __init__(self, *args, **kwargs):
        """class constructon"""
        self.place_id = kwargs.pop('place_id', "")
        self.user_id = kwargs.pop('user_id', "")
        self.text = kwargs.pop('text', "")
        super().__init__(*args, **kwargs)
