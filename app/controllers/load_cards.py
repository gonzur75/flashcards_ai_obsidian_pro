from app.db.db import DBTiny
from app.models.flashcard_models import FlashCardSrc
from app.settings.settings import dirname_app


def load_cards() -> list[FlashCardSrc]:
    with DBTiny(dirname_app / '.store', 'flashcards') as db:
        cards = db.read_all()

    return [FlashCardSrc(**card) for card in cards]