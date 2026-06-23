from collections.abc import Iterable
from typing import Any

from david8.protocols.sql import FunctionProtocol, LogicalOperatorProtocol, PredicateProtocol
from david8.protocols.sql import QueryProtocol as _QueryProtocol
from david8.protocols.sql import SelectProtocol as _SelectProtocol


class SelectProtocol(_SelectProtocol):
    def from_csv(self, *file_names: str) -> 'SelectProtocol':
        pass

    def from_json(self, *file_names: str) -> 'SelectProtocol':
        pass

    def from_json_objects(self, *file_names: str) -> 'SelectProtocol':
        pass

    def from_ndjson_objects(self, *file_names: str) -> 'SelectProtocol':
        pass

    def from_json_objects_auto(self, *file_names: str) -> 'SelectProtocol':
        pass

    def from_parquet(self, *file_names: str) -> 'SelectProtocol':
        pass

    def from_xlsx(self, file_name: str) -> 'SelectProtocol':
        pass


class MergeIntoProtocol(_QueryProtocol):
    def using(self, query: SelectProtocol, as_: str, columns: Iterable[str] | None = None) -> 'MergeIntoProtocol':
        pass

    def on(self, *args: LogicalOperatorProtocol | PredicateProtocol) -> 'MergeIntoProtocol':
        pass

    def update_when_matched(
        self,
        operator: LogicalOperatorProtocol | None = None,
        columns: dict[str, Any] | None = None,
    ) -> 'MergeIntoProtocol':
        pass

    def delete_when_matched(self, operator: LogicalOperatorProtocol) -> 'MergeIntoProtocol':
        pass

    def returning(self, *args: str) -> 'MergeIntoProtocol':
        pass

    def insert_when_not_matched(self) -> 'MergeIntoProtocol':
        pass


class PivotProtocol(_QueryProtocol):
    def on(self, *columns: str) -> 'PivotProtocol':
        pass

    def using(self, *values: FunctionProtocol) -> 'PivotProtocol':
        pass

    def group_by(self, *columns: str) -> 'PivotProtocol':
        pass

    def order_by(self, *columns: str, desc: bool = True) -> 'PivotProtocol':
        pass

    def limit(self, value: int) -> 'PivotProtocol':
        pass


class UnpivotProtocol(_QueryProtocol):
    def into(self, name: str, value: str | Iterable[str]) -> 'UnpivotProtocol':
        pass

    def on(self, *columns: str) -> 'UnpivotProtocol':
        pass

    def order_by(self, *columns: str, desc: bool = True) -> 'UnpivotProtocol':
        pass

    def limit(self, value: int) -> 'UnpivotProtocol':
        pass
