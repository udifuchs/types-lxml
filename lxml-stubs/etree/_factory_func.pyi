from .._types import (
    _ET,
    SupportsLaxedItems,
    _AnyStr,
    _NSMapArg,
    _TagName,
)
from ._element import _Comment, _Entity, _ProcessingInstruction

def Comment(text: _AnyStr | None = ...) -> _Comment: ...
def ProcessingInstruction(
    target: _AnyStr, text: _AnyStr | None = ...
) -> _ProcessingInstruction: ...

PI = ProcessingInstruction

def Entity(name: _AnyStr) -> _Entity: ...

def SubElement(
    _parent: _ET,
    _tag: _TagName,
    /,
    attrib: SupportsLaxedItems[str, _AnyStr] | None = ...,
    nsmap: _NSMapArg | None = ...,
    **_extra: _AnyStr,
) -> _ET: ...
