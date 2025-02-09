import re
from datetime import datetime

import pytest

from app.models.note_models import Note


def test_empty_title_raises_value_error():
    with pytest.raises(ValueError, match="Title: '' must be a none-empty string."):
        _ = Note(title="", content="", tags={"python", "pytest"}, updated_at=datetime.now())


def test_empty_content_raise_value_error():
    with pytest.raises(ValueError, match=re.escape("Content: '' must be a none-empty string.")):
        _ = Note(
            title="Note title",
            content="",
            tags={"python", "pytest"},
            updated_at=datetime.now(),
        )


def test_empty_tags_raise_value_error():
    with pytest.raises(ValueError, match=re.escape("Tags: set() must be a none-empty set.")):
        _ = Note(
            title="Note title",
            content="Note content",
            tags=set(),
            updated_at=datetime.now(),
        )


def test_tags_with_empty_values_rise_value_error() -> None:
    with pytest.raises(ValueError, match=re.escape("Tags: set() must be a none-empty set.")):
        Note(title="Title", content="Note content", tags={"", "  "}, updated_at=datetime.now())


def test_tags_are_striped() -> None:
    note = Note(title="Title", content="Note content", tags={"python  ", "  pytest"}, updated_at=datetime.now())
    assert note.tags == {"python", "pytest"}


def test_tags_are_lowercase() -> None:
    note = Note(title="Title", content="Note content", tags={"Python", "  pyTest"}, updated_at=datetime.now())

    assert note.tags == {"python", "pytest"}
