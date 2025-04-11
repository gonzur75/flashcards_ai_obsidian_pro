import time
from typing import Iterator

import typer
from rich.table import Table
from typer import Typer
from rich import print
from rich.console import Console

from app.controllers.create_cards import create_cards
from app.controllers.save_cards import save_cards
# from app.models.flashcard_models import FlashCard
from app.controllers.load_cards import load_cards
from app.logging_configs.logging_setup import setup_logging

app: Typer = Typer(add_completion=False)
console: Console = Console()


# _dirname = Path(__file__).parent



@app.callback(invoke_without_command=True)
def menu() -> None:
    setup_logging()

    print("Choose option:")
    print("1. Create cards from Vault")
    print("2. Get cards from DB")
    print("3. Create Deck")

    choice = typer.prompt("Provide option number", type=int)

    if choice == 1:
        cards = create_cards_cli()
        option = typer.confirm("Save to db?")
        if option:
            save_cards_cli(cards)
        menu()
    elif choice == 2:
        get_cards_cli()
    elif choice == 3:
        print("Creating deck")
    else:
        print("Thank you for using Flashcards AI")


def save_cards_cli(cards: list) -> None:
    save_cards(cards)


def flat_if(cards: list) -> Iterator:
    for card in cards:
        if not isinstance(card, dict):
            yield from flat_if(card)
        else:
            yield card


@app.command(name="create-cards")
def create_cards_cli() -> list:
    total = 100
    with typer.progressbar(range(total), label="Generating...") as progress:
        for _ in progress:
            time.sleep(0.01)

    cards = create_cards()
    table = Table("Question", "Level")

    with typer.progressbar(range(100), label="Transforming...") as progress:
        for _ in progress:
            time.sleep(0.01)

    for card in cards:
        table.add_row(card.front_site, card.difficulty_level.value)

    console.print(table)
    return cards


@app.command(name="get-cards")
def get_cards_cli() -> None:
    cards = load_cards()
    table = Table("Question", "Level", title="Flashcards AI")
    for card in cards:
        table.add_row(card["front_site"], card["difficulty_level"])


# @app.command(name="create-deck")
# def create_deck_cli() -> None:
#     name = typer.prompt("Enter deck name:")
#     indexes = typer.prompt("Provide indexes for deck, comma seperated", type=str)
#     indexes_digits = (int(digit) for digiit in re.findall("\d+", indexes))
#
#     cards = get_cards_by_id(indexes_digits)
#     print(cards)

if __name__ == "__main__":

    app()
