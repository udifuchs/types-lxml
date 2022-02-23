from typing import Any, Callable, Dict, List, Mapping, Optional, Tuple, Union

from .etree import _Element

# ElementTree API is notable of canonicalizing byte / unicode input data.
# Not to be confused with typing.AnyStr which is TypeVar.
_AnyStr = Union[str, bytes]

_ListAnyStr = Union[List[str], List[bytes]]
_DictAnyStr = Union[Dict[str, str], Dict[bytes, bytes]]
_Dict_Tuple2AnyStr_Any = Union[Dict[Tuple[str, str], Any], Tuple[bytes, bytes], Any]

# See https://github.com/python/typing/pull/273
# Due to Mapping having invariant key types, Mapping[Union[A, B], ...]
# would fail to validate against either Mapping[A, ...] or Mapping[B, ...]
# Try to settle for simpler solution, assuming users would not use byte
# string as namespace prefix.
_NSMapArg = Optional[
    Union[
        Mapping[None, _AnyStr],
        Mapping[str, _AnyStr],
        Mapping[Optional[str], _AnyStr],
    ]
]
_NonDefaultNSMapArg = Optional[Mapping[str, _AnyStr]]

_ExtensionArg = Optional[
    Mapping[
        Tuple[Optional[_AnyStr], _AnyStr],
        Callable[..., Any],  # TODO extension function not investigated yet
    ]
]

# XPathObject documented in https://lxml.de/xpathxslt.html#xpath-return-values
# However the type is too versatile to be of any use in further processing,
# so users are encouraged to do type narrowing by themselves.
_XPathObject = Any
# XPath variable supports most of the XPathObject types
# as _input_ argument value, but most users would probably
# only use primivite types for substitution.
_XPathVarArg = Union[
    bool,
    int,
    float,
    _AnyStr,
    _Element,
    list[_Element],
]
