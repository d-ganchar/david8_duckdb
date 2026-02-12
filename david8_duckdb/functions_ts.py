import dataclasses

from david8.core.fn_generator import FnCallableFactory as _FnCallableFactory
from david8.core.fn_generator import SeparatedArgsFn as _SeparatedArgsFn
from david8.expressions import col as _col
from david8.protocols.sql import ExprProtocol, FunctionProtocol


@dataclasses.dataclass(slots=True)
class _AgeFactory(_FnCallableFactory):
    def __call__(self, start: str | ExprProtocol, end: str | ExprProtocol) -> FunctionProtocol:
        args = (
            _col(start) if isinstance(start, str) else start,
            _col(end) if isinstance(end, str) else end,
        )

        return _SeparatedArgsFn(self.name, fn_items=args, separator=', ')


age = _AgeFactory(name='age')
