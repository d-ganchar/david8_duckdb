from david8_duckdb.functions_ts import age
from tests.base_test import BaseTest


class TestFunctionsTs(BaseTest):
    def test_age(self):
        self.assertEqual(
            BaseTest.qb.select(age('start', 'end')).get_sql(),
            'SELECT age(start, end)'
        )
