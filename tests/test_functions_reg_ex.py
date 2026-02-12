from david8.expressions import val
from david8.protocols.sql import FunctionProtocol
from parameterized import parameterized

from david8_duckdb.functions_reg_ex import regexp_extract_all
from tests.base_test import BaseTest


class TestFunctionsRegEx(BaseTest):
    @parameterized.expand([
        (
            regexp_extract_all('column_name', r'(\w+):\s*(\d+)'),
            "SELECT regexp_extract_all(column_name, '(\\w+):\\s*(\\d+)')",
        ),
        (
            regexp_extract_all(val('Peter: 33, Paul:14'), r'(\w+):\s*(\d+)', 2).as_('age'),
            "SELECT regexp_extract_all('Peter: 33, Paul:14', '(\\w+):\\s*(\\d+)', 2) AS age",
        ),
    ])
    def test_regexp_extract_all(self, fn: FunctionProtocol, exp_sql: str):
        self.assertEqual(BaseTest.qb.select(fn).get_sql(), exp_sql)
