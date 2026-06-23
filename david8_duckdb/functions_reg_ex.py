"""
Deprecated since 0.5.0b1. Will be removed in 0.1.0
Use `functions` module instead, example:
from david8.functions import regexp_extract_all
"""
from david8_duckdb.core.fn_generator import RegexpExtractAllFactory as _RegexpExtractAllFactory

regexp_extract_all = _RegexpExtractAllFactory(name='regexp_extract_all')
