"""Unit tests."""

from typing import Annotated

import pytest

from is_annotated import isannotated


@pytest.mark.parametrize(
    ("obj", "expected"),
    [
        (1, False),
        (int, False),
        (Annotated[int, "2"], True),
        (Annotated[int, 1, "2"], True),
    ],
    ids=lambda x: type(x).__name__,
)
def test_is_annotated(obj, expected):
    """Test ``isannotated`` function."""
    assert isannotated(obj) is expected
