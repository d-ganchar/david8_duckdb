from david8.core.fn_generator import OneArgWindowFactory as _OneArgWindowFactory

from david8_duckdb.core.fn_generator import AgeFactory as _AgeFactory
from david8_duckdb.core.fn_generator import JsonWithPathFactory as _JsonWithPathFactory
from david8_duckdb.core.fn_generator import RegexpExtractAllFactory as _RegexpExtractAllFactory

# timestamp functions
age = _AgeFactory(name='age')

# regexp functions
regexp_extract_all = _RegexpExtractAllFactory(name='regexp_extract_all')

# json functions
json_keys = _JsonWithPathFactory(name='json_keys')
json_extract = _JsonWithPathFactory(name='json_extract')

# agg functions
entropy = _OneArgWindowFactory(name='entropy')
kurtosis = _OneArgWindowFactory(name='kurtosis')
skewness = _OneArgWindowFactory(name='skewness')
