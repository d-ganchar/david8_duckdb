from david8.protocols.sql import FunctionProtocol
from parameterized import parameterized

from david8_duckdb.functions_json import json_keys
from tests.base_test import BaseTest


class TestFunctionsJson(BaseTest):
    @parameterized.expand([
        (
            json_keys('column_name'),
            'SELECT json_keys(column_name)',
        ),
        (
            json_keys('column_name', '$.ducks.country'),
            "SELECT json_keys(column_name, '$.ducks.country')",
        ),
    ])
    def test_json_keys(self, fn: FunctionProtocol, exp_sql: str):
        self.assertEqual(BaseTest.qb.select(fn).get_sql(), exp_sql)
