from david8.expressions import val as v
from david8.functions import trim
from david8.predicates import is_null
from david8.protocols.sql import ExprProtocol
from parameterized import parameterized

from david8_duckdb.expressions import columns, exclude, rename, replace
from tests.base_test import BaseTest


class TestStarExpression(BaseTest):
    def test_exclude(self):
        self.assertEqual(
            self.qb.select(exclude('salary', 'ssn')).get_sql(),
            'SELECT * EXCLUDE (salary, ssn)'
        )

    def test_replace(self):
        self.assertEqual(
            self.qb.select(replace(
                trim('col1').as_('col1'),
                trim('col2').as_('col2'),
            )).get_sql(),
            'SELECT * REPLACE (trim(col1) AS col1, trim(col2) AS col2)'
        )

    def test_rename(self):
        self.assertEqual(
            self.qb.select(rename(
                ('a', 'b'),
                ('c', 'd'),
            )).get_sql(),
            'SELECT * RENAME (a AS b, c AS d)'
        )

    @parameterized.expand([
        (
            columns('*'),
            'SELECT COLUMNS(*)',
        ),
        (
            columns(v('(id|numbers?)')),
            "SELECT COLUMNS('(id|numbers?)')",
        ),
        (
            trim(columns('*')),
            'SELECT trim(COLUMNS(*))',
        ),
        (
            is_null(columns('*')),
            'SELECT COLUMNS(*) IS NULL',
        ),
    ])
    def test_export_db(self, expr: ExprProtocol, exp_sql: str):
        self.assertEqual(self.qb.select(expr).get_sql(), exp_sql)
