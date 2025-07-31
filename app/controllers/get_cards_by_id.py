import typer

from app.db.db import DBTiny
from app.models.flashcard_models import FlashCardId
from app.settings.settings import dirname_app


def get_cards_by_id(indexes: list[int]) -> list[FlashCardId]:
    with DBTiny(dirname_app / '.store', db_file_prefix='flashcards') as db:
        cards = db.get(indexes)
    typer.echo([card.doc_id for card in  cards])
    return [FlashCardId(id=card.doc_id, **card) for card in cards]