from typing import overload, TypeVar
from typing_extensions import Self

from .._types import (
    _ET,
    SupportsLaxedItems,
    _AnyStr,
    _ET_co,
    _ETT,
    _ETT_co,
    _FileReadSource,
    _NSMapArg,
    _TagName,
)
from ._element import _Comment, _Element, _ElementTree, _Entity, _ProcessingInstruction
from ._parser import _DefEtreeParsers

def Comment(text: _AnyStr | None = ...) -> _Comment: ...
def ProcessingInstruction(
    target: _AnyStr, text: _AnyStr | None = ...
) -> _ProcessingInstruction: ...

PI = ProcessingInstruction

def Entity(name: _AnyStr) -> _Entity: ...

class Element(_Element):
    def __new__(  # Args identical to _Element.makeelement
        cls,
        _tag: _TagName,
        /,
        attrib: SupportsLaxedItems[str, _AnyStr] | None = ...,
        nsmap: _NSMapArg | None = ...,
        **_extra: _AnyStr,
    ) -> Self: ...

def SubElement(
    _parent: _ET,
    _tag: _TagName,
    /,
    attrib: SupportsLaxedItems[str, _AnyStr] | None = ...,
    nsmap: _NSMapArg | None = ...,
    **_extra: _AnyStr,
) -> _ET: ...

class ElementTree(_ElementTree[_ET_co]):
    @overload  # from element, parser ignored
    def __new__(cls: type[_ETT], element: _ET) -> _ETT: ...
    @overload  # from file source, custom parser
    def __new__(
        cls: type[_ETT_co],
        element: None = ...,
        *,
        file: _FileReadSource,
        parser: _DefEtreeParsers[_ET_co],
    ) -> _ETT_co: ...
    @overload  # from file source, default parser
    def __new__(
        cls: type[_ETT],
        element: None = ...,
        *,
        file: _FileReadSource,
        parser: None = ...,
    ) -> _ETT: ...
