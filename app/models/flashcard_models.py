from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=False, kw_only=True, slots=True)
class Flashcard:
    question: str
    answer: str
    tags: set[str]
    updated_at: datetime

    def __post_init__(self):
        if not self.question:
            raise ValueError(f"Question: {self.question!r} must be a non-empty string.")

        if not self.answer:
            raise ValueError(f"Answer: {self.answer!r} must be a non-empty string.")

        if not self.tags:
            raise ValueError(f"Tags: {self.tags!r} must be a none-empty set.")

        self.tags = {tag.strip().lower() for tag in self.tags if tag.strip()}

        if not self.tags:
            raise ValueError(f"Tags: {self.tags!r} must be a none-empty set.")