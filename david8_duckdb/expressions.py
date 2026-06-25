from david8.expressions import col as c
from david8.protocols.sql import ExprProtocol, FunctionProtocol

from david8_duckdb.base_expressions import BaseColumnsExpression as _BaseColumnsExpression
from david8_duckdb.base_expressions import BaseStarExpression as _BaseStarExpression


def exclude(*args: str) -> ExprProtocol:
    return _BaseStarExpression(_clause_name = 'EXCLUDE', _args=args)


def replace(*args: FunctionProtocol) -> ExprProtocol:
    return _BaseStarExpression(_clause_name='REPLACE', _args=args)


def rename(*args: tuple[str, str]) -> ExprProtocol:
    converted = tuple(c(col).as_(alias) for col, alias in args)
    return _BaseStarExpression(_clause_name='RENAME', _args=converted)


def columns(*args: str | ExprProtocol) -> ExprProtocol:
    return _BaseColumnsExpression(_args=args)
