"""
Deprecated since 0.5.0b1. Will be removed in 0.1.0
Use `functions` module instead, example:
from david8.functions import json_keys
"""
from david8_duckdb.core.fn_generator import JsonWithPathFactory as _JsonWithPathFactory

json_keys = _JsonWithPathFactory(name='json_keys')
json_extract = _JsonWithPathFactory(name='json_extract')
