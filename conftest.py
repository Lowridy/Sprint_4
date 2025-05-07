import pytest
from main import BooksCollector

@pytest.fixture
def new_collector():
    return BooksCollector()

@pytest.fixture
def collector_with_books():
    collector = BooksCollector()
    books = [
        ("Гарри Поттер", "Фантастика"),
        ("Оно", "Ужасы"),
        ("Шерлок Холмс", "Детективы")
    ]
    for name, genre in books:
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return collector

@pytest.fixture
def collector_with_favorites():
    """Создает экземпляр с 2 книгами в избранном."""
    collector = BooksCollector()
    books = ["Гарри Поттер", "Шерлок Холмс"]
    for name in books:
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
    return collector