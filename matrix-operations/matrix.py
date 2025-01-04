from abc import ABC, abstractmethod
from typing import Generic
from ctypes import py_object
from typing import TypeVar, Generic

class Matrix:
    """A class represents a mathematical matrix defined by m columns and n rows"""
    def __init__(self, content=[], columns=0, rows=0):
        self.content = content 
        self.columns = columns
        self.rows = rows
    def is_valid(self):
        """Return a Boolean to confirm validity of a matrix"""
        if len(self.content) // self.columns == 0 and len(self.content) // self.columns == self.rows:
           return True
        return False 
    def __len__(self):
        """Total entries of the matrix"""
        return len(self.content)
    def __str__(self):
        return f"{self.rows} x {self.columns} matrix"

