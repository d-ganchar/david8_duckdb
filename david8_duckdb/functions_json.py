import dataclasses

from david8.core.fn_generator import FnCallableFactory as _FnCallableFactory
from david8.core.fn_generator import SeparatedArgsFn as _SeparatedArgsFn
from david8.expressions import col as _col
from david8.expressions import val as _val
from david8.protocols.sql import ExprProtocol, FunctionProtocol


@dataclasses.dataclass(slots=True)
class _JsonWithPathFactory(_FnCallableFactory):
    def __call__(self, column: str | ExprProtocol, path_value: str = '') -> FunctionProtocol:
        args = (_col(column) if isinstance(column, str) else column, )
        if path_value:
            args += (_val(path_value), )

        return _SeparatedArgsFn(self.name, fn_items=args, separator=', ')


json_keys = _JsonWithPathFactory(name='json_keys')
