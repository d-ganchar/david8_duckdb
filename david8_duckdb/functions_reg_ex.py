import dataclasses

from david8.core.fn_generator import FnCallableFactory as _FnCallableFactory
from david8.core.fn_generator import SeparatedArgsFn as _SeparatedArgsFn
from david8.expressions import col as _col
from david8.expressions import val as _val
from david8.protocols.sql import ExprProtocol, FunctionProtocol


@dataclasses.dataclass(slots=True)
class _RegexpExtractAllFactory(_FnCallableFactory):
    def __call__(self, column: str | ExprProtocol, regex: str, group: int = None) -> FunctionProtocol:
        args = (
            _col(column) if isinstance(column, str) else column,
            _val(regex)
        )

        if isinstance(group, int):
            args += (_val(group), )

        return _SeparatedArgsFn(self.name, fn_items=args, separator=', ')


regexp_extract_all = _RegexpExtractAllFactory(name='regexp_extract_all')
