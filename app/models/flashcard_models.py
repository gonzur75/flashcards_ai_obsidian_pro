from dataclasses import dataclass
from enum import Enum


class DifficultyEnum(Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"


class NonEmptyString(str):
    def __new__(cls, value: str):
        if not value.strip():
            raise ValueError("String must be non-empty.")
        return super().__new__(cls, value)


@dataclass(frozen=False, kw_only=True, slots=True)
class FlashCardSrc:
    difficulty_level: DifficultyEnum
    tags: list[NonEmptyString]
    front_site: NonEmptyString
    back_site: NonEmptyString
    origin: NonEmptyString


@dataclass(frozen=False, kw_only=True, slots=True)
class FlashCardId(FlashCardSrc):
    id: int

