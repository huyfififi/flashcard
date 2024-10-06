import json

from flashcard.models import FlashCard


FLASHCARD_QUESTIONS_PATH = "src/resources/civics_100q.json"


def load_flashcards(file_path: str) -> tuple[FlashCard]:
    with open(file_path, "r") as f:
        data = json.load(f)
    return tuple(FlashCard(**flashcard) for flashcard in data)


def main():
    flashcards: tuple[FlashCard] = load_flashcards(FLASHCARD_QUESTIONS_PATH)
    for flashcard in flashcards:
        print(f"Question: {flashcard.question}")
        print(f"Answer: {flashcard.answer}")
        print()
