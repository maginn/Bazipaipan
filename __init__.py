"""
BaZi Calculator Package

A Python package for BaZi (八字) fortune calculation based on Shouxing astronomical calendar.

This package provides:
1. Encapsulation of Heavenly Stems, Earthly Branches, Four Pillars, Ten Gods, Five Elements
2. Rule library supporting: Heavenly Stems five combinations, clashes, restrictions,
   Earthly Branches punishment, clash, combination, harm, three meetings, three combinations
"""

__version__ = "1.0.0"
__author__ = "BaZi Project"

# Import main classes for easy access
from .BZPaipan import BzPaipan
from .BzRules import Bzrules
from .BzBaseClass import *

__all__ = [
    'BzPaipan',
    'Bzrules',
]