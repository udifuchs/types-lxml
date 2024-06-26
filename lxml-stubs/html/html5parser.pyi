#
# Note that this interface only generates lxml.etree Elements, not lxml.html ones
# See https://github.com/html5lib/html5lib-python/issues/102
#

from _typeshed import SupportsRead
from typing import Literal, overload

import html5lib as _html5lib

from .._types import _AnyStr
from ..etree import _Element, _ElementTree

# Note that tree arg is dropped, because the sole purpose of using
# this parser is to generate lxml element tree with html5lib parser.
# Other arguments good for html5lib >= 1.0
class HTMLParser(_html5lib.HTMLParser):
    def __init__(
        self,
        strict: bool = False,
        namespaceHTMLElements: bool = True,
        debug: bool = False,
    ) -> None: ...

html_parser: HTMLParser

# Notes:
# - No XHTMLParser here. Lxml tries to probe for some hypothetical
#   XHTMLParser class in html5lib which had never existed.
#   The core probing logic of this user-contributed submodule has never
#   changed since last modification at 2010. Probably yet another
#   member of code wasteland.
# - Exception raised for the combination html=<str> and guess_charset=True,
#   but not reflected here. (TODO or?)
# - Although other types of parser _might_ be usable (after implementing
#   parse() method, that is), such usage completely defeats the purpose of
#   creating this submodule. It is intended for subclassing or
#   init argument tweaking instead.

def document_fromstring(
    html: _AnyStr, guess_charset: bool | None = None, parser: HTMLParser | None = None
) -> _Element: ...
@overload
def fragments_fromstring(  # type: ignore
    html: _AnyStr,
    no_leading_text: Literal[True],
    guess_charset: bool | None = None,
    parser: HTMLParser | None = None,
) -> list[_Element]: ...

# The first item in the list may be a string
@overload
def fragments_fromstring(
    html: _AnyStr,
    no_leading_text: bool = False,
    guess_charset: bool | None = None,
    parser: HTMLParser | None = None,
) -> list[str | _Element]: ...
def fragment_fromstring(
    html: _AnyStr,
    create_parent: bool | _AnyStr = False,
    guess_charset: bool | None = None,
    parser: HTMLParser | None = None,
) -> _Element: ...
def fromstring(
    html: _AnyStr,
    guess_charset: bool | None = None,
    parser: HTMLParser | None = None,
) -> _Element: ...
def parse(
    # html5lib doesn't support pathlib
    filename_url_or_file: _AnyStr | SupportsRead[bytes] | SupportsRead[str],
    guess_charset: bool | None = None,
    parser: HTMLParser | None = None,
) -> _ElementTree: ...
