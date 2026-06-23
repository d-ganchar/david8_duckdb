"""
Deprecated since 0.5.0b1. Will be removed in 0.1.0
Use `functions` module instead, example:
from david8.functions import age
"""
from david8_duckdb.core.fn_generator import AgeFactory as _AgeFactory

age = _AgeFactory(name='age')
