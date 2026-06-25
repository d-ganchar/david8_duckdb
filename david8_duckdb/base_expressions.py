import dataclasses

from david8.core.arg_convertors import to_col_or_expr as _to_col_or_expr
from david8.protocols.dialect import DialectProtocol
from david8.protocols.sql import AliasedProtocol, ExprProtocol, FunctionProtocol


@dataclasses.dataclass(slots=True)
class BaseStarExpression(ExprProtocol):
    _clause_name: str
    _args: tuple[str | FunctionProtocol | AliasedProtocol,...] = dataclasses.field(default_factory=tuple)

    def get_sql(self, dialect: DialectProtocol) -> str:
        items = ', '.join(_to_col_or_expr(i, dialect) for i in self._args)
        return f'* {self._clause_name} ({items})'


@dataclasses.dataclass(slots=True)
class BaseColumnsExpression(ExprProtocol):
    _args: tuple[str | FunctionProtocol | AliasedProtocol,...] = dataclasses.field(default_factory=tuple)

    def get_sql(self, dialect: DialectProtocol) -> str:
        items = ', '.join(_to_col_or_expr(i, dialect) for i in self._args)
        return f'COLUMNS({items})'
