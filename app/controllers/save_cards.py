from dataclasses import asdict

from app.db.db import DBTiny
from app.models.flashcard_models import FlashCardSrc
from app.settings.settings import dirname_app


def save_cards(cards: list[FlashCardSrc]) -> None:
    with DBTiny(dirname_app / '.store', db_file_prefix='flashcards') as db:
        bulk_create = []
        for card in cards:
            data = asdict(card)
            data['difficulty_level'] = card.difficulty_level.value
            bulk_create.append(data)
        db.create_many(bulk_create)
