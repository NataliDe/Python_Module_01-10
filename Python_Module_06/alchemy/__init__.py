"""
A simple module for creating basic elemental objects.

This module provides functions for creating fire and water elements.
"""

__version__ = "1.0.0"
__author__ = "Master Pythonicus"

from .elements import create_fire, create_water

__all__ = [
    "create_fire",
    "create_water",
]
