from dataclasses import dataclass


@dataclass(frozen=False, kw_only=True, slots=True)
class DeckSrc:
    name: str
    description: str
    cards: list[int]