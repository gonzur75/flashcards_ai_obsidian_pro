import re

import pytest
from datetime import datetime

from app.models.flashcard_models import Flashcard


def test_flashcard_creation_with_valid_data():
    flashcard = Flashcard(
        question="What is Python?",
        answer="A programming language.",
        tags={"programming", "python"},
        updated_at=datetime.now(),
    )
    assert flashcard.question == "What is Python?"
    assert flashcard.answer == "A programming language."
    assert flashcard.tags == {"programming", "python"}


def test_flashcard_creation_with_empty_question():
    with pytest.raises(ValueError, match="Question: '' must be a non-empty string."):
        Flashcard(
            question="", answer="A programming language.", tags={"programming", "python"}, updated_at=datetime.now()
        )


def test_flashcard_creation_with_empty_answer():
    with pytest.raises(ValueError, match="Answer: '' must be a non-empty string."):
        Flashcard(question="What is Python?", answer="", tags={"programming", "python"}, updated_at=datetime.now())


def test_flashcard_creation_with_empty_tags():
    with pytest.raises(ValueError, match=re.escape("Tags: set() must be a none-empty set.")):
        Flashcard(question="What is Python?", answer="A programming language.", tags=set(), updated_at=datetime.now())


def test_flashcard_creation_with_whitespace_tags():
    flashcard = Flashcard(
        question="What is Python?",
        answer="A programming language.",
        tags={"  programming  ", "  python  "},
        updated_at=datetime.now(),
    )
    assert flashcard.tags == {"programming", "python"}
