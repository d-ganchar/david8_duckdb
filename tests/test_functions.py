from david8.expressions import val
from david8.protocols.sql import FunctionProtocol
from parameterized import parameterized

from david8_duckdb.functions import age, entropy, json_extract, json_keys, kurtosis, regexp_extract_all, skewness
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
        (
            json_extract('column_name', '$.ducks.country[0]'),
            "SELECT json_extract(column_name, '$.ducks.country[0]')",
        ),
    ])
    def test_json_function(self, fn: FunctionProtocol, exp_sql: str):
        self.assertEqual(BaseTest.qb.select(fn).get_sql(), exp_sql)


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


class TestFunctionsTs(BaseTest):
    def test_age(self):
        self.assertEqual(
            BaseTest.qb.select(age('start', 'end')).get_sql(),
            'SELECT age(start, end)'
        )


class TestAggFunctions(BaseTest):
    @parameterized.expand([
        (
            entropy('category').over(partition_by=['user_id'], order_by=['ts']),
            'SELECT entropy(category) OVER (PARTITION BY user_id ORDER BY ts)',
        ),
    ])
    def test_entropy(self, fn: FunctionProtocol, exp_sql: str):
        query = self.qb.select(fn)
        self.assertEqual(query.get_sql(), exp_sql)

    @parameterized.expand([
        (
            kurtosis('category').over(partition_by=['user_id'], order_by=['ts']),
            'SELECT kurtosis(category) OVER (PARTITION BY user_id ORDER BY ts)',
        ),
    ])
    def test_kurtosis(self, fn: FunctionProtocol, exp_sql: str):
        query = self.qb.select(fn)
        self.assertEqual(query.get_sql(), exp_sql)

    @parameterized.expand([
        (
            skewness('category').over(partition_by=['user_id'], order_by=['ts']),
            'SELECT skewness(category) OVER (PARTITION BY user_id ORDER BY ts)',
        ),
    ])
    def test_skewness(self, fn: FunctionProtocol, exp_sql: str):
        query = self.qb.select(fn)
        self.assertEqual(query.get_sql(), exp_sql)
