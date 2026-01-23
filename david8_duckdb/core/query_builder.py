from david8.core.base_query_builder import BaseQueryBuilder as _BaseQueryBuilder
from david8.protocols.sql import AliasedProtocol, ExprProtocol, FunctionProtocol

from .select_query import DuckDbSelect
from ..protocols.query_builder import QueryBuilderProtocol
from ..protocols.sql import SelectProtocol


class DuckDbQueryBuilder(QueryBuilderProtocol, _BaseQueryBuilder):
    def select(self, *args: str | AliasedProtocol | ExprProtocol | FunctionProtocol) -> SelectProtocol:
        return DuckDbSelect(select_columns=args, dialect=self._dialect)
