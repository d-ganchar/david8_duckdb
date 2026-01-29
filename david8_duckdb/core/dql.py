import dataclasses

from david8.core.base_query import BaseQuery
from david8.protocols.dialect import DialectProtocol
from david8.protocols.sql import FunctionProtocol

from david8_duckdb.protocols.sql import PivotProtocol


@dataclasses.dataclass(slots=True)
class PivotQuery(BaseQuery, PivotProtocol):
    table: str
    on_columns: tuple[str, ...] = dataclasses.field(default_factory=tuple)
    group_by_columns: tuple[str, ...] = dataclasses.field(default_factory=tuple)
    order_by_columns: tuple[tuple[bool, tuple[str, ...]], ...] = dataclasses.field(default_factory=tuple)
    using_values: tuple[FunctionProtocol, ...] = dataclasses.field(default_factory=tuple)
    limit_value: int | None = None

    def on(self, *columns: str) -> 'PivotProtocol':
        self.on_columns = columns
        return self

    def using(self, *values: FunctionProtocol) -> 'PivotProtocol':
        self.using_values = values
        return self

    def group_by(self, *columns: str) -> 'PivotProtocol':
        self.group_by_columns = columns
        return self

    def order_by(self, *columns: str, desc: bool = True) -> 'PivotProtocol':
        self.order_by_columns += ((desc, columns, ), )
        return self

    def limit(self, value: int) -> 'PivotProtocol':
        self.limit_value = value
        return self

    def _render_sql(self, dialect: DialectProtocol) -> str:
        items = ['PIVOT', dialect.quote_ident(self.table)]
        if self.on_columns:
            items.append('ON')
            items.append(', '.join(dialect.quote_ident(c) for c in self.on_columns))

        if self.using_values:
            items.append('USING')
            items.append(', '.join(c.get_sql(dialect) for c in self.using_values))

        if self.group_by_columns:
            items.append('GROUP BY')
            items.append(', '.join(dialect.quote_ident(c) for c in self.group_by_columns))

        if self.order_by_columns:
            items.append('ORDER BY')
            order_items = []
            for desc, columns in self.order_by_columns:
                for column in columns:
                    order_items.append(f'{dialect.quote_ident(column)}{" DESC" if desc else ""}')

            items.append(', '.join(order_items))

        if self.limit_value:
            items.append(f'LIMIT {self.limit_value}')

        return ' '.join(items)
