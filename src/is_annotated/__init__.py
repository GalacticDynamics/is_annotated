"""Copyright (c) 2024 Nathaniel Starkman. All rights reserved.

is_annotated: Check if a type hint is an `Annotated` type.
"""

__all__ = ["isannotated"]

from typing import Annotated

from typing_extensions import TypeGuard, _AnnotatedAlias

AnnotationType = type(Annotated[int, "_"])


def isannotated(hint: object, /) -> TypeGuard[_AnnotatedAlias]:
    """Check if a type hint is an `Annotated` type.

    Examples
    --------
    >>> from is_annotated import isannotated

    >>> isannotated(int)
    False

    >>> from typing import Annotated
    >>> isannotated(Annotated[int, "2"])
    True

    """
    return type(hint) is AnnotationType  # pylint: disable=unidiomatic-typecheck
