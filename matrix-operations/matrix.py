from abc import ABC, abstractmethod
from typing import Generic
from ctypes import py_object
from typing import TypeVar, Generic
import pdb

class Matrix:
    """A class represents a mathematical matrix defined by m columns and n rows"""
    def __init__(self, content=[], rows=0, columns=0):
        self.content = content
        self.rows = rows 
        self.columns = columns
    def is_valid(self):
        """Return a Boolean to confirm validity of a matrix"""
        return (len(self.content) % self.columns) == 0 and (len(self.content) // self.columns) == self.rows
    def __len__(self):
        """Total entries of the matrix"""
        return len(self.content)
    def __str__(self):
        return f"{self.rows} x {self.columns} Matrix"

