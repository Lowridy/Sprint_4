import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2 # Похоже в первоначальном примере была опечатка, исправил

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

 # Тест 2: Нельзя добавить дубликат книги
    def test_add_duplicate_book(self, new_collector):
        new_collector.add_new_book("Дубликат")
        new_collector.add_new_book("Дубликат")
        assert len(new_collector.books_genre) == 1

    # Тест 3: Установка жанра для существующей книги
    def test_set_book_genre_valid(self, collector_with_books):
        collector_with_books.set_book_genre("Гарри Поттер", "Мультфильмы")
        assert collector_with_books.get_book_genre("Гарри Поттер") == "Мультфильмы"

    # Тест 4: Нельзя установить несуществующий жанр
    def test_set_invalid_genre(self, collector_with_books):
        collector_with_books.set_book_genre("Гарри Поттер", "Несуществующий жанр")
        assert collector_with_books.get_book_genre("Гарри Поттер") == "Фантастика"

    # Тест 5: Получение книг по жанру
    def test_get_books_by_genre(self, collector_with_books):
        fantasy_books = collector_with_books.get_books_with_specific_genre("Фантастика")
        assert "Гарри Поттер" in fantasy_books
        assert len(fantasy_books) == 1

    # Тест 6: Книги для детей (проверка с параметризацией)
    @pytest.mark.parametrize("book_name, genre", [
        ("Гарри Поттер", "Фантастика"),
        ("Ну, погоди!", "Мультфильмы")
    ])
    def test_children_books_with_allowed_genres(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert book_name in collector.get_books_for_children()

    @pytest.mark.parametrize("book_name, genre", [
        ("Оно", "Ужасы"),
        ("Шерлок Холмс", "Детективы")
        ])
    def test_adult_books_not_for_children(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert book_name not in collector.get_books_for_children()

    # Тест 7: Добавление в избранное
    def test_add_to_favorites(self, collector_with_books):
        collector_with_books.add_book_in_favorites("Гарри Поттер")
        assert "Гарри Поттер" in collector_with_books.get_list_of_favorites_books()

    # Тест 8: Нельзя добавить в избранное дважды
    def test_add_to_favorites_twice(self, collector_with_favorites):
        initial_count = len(collector_with_favorites.get_list_of_favorites_books())
        collector_with_favorites.add_book_in_favorites("Гарри Поттер")  # Пытаемся добавить существующее
        assert len(collector_with_favorites.get_list_of_favorites_books()) == initial_count

    # Тест 9: Удаление из избранного
    def test_remove_from_favorites(self, collector_with_favorites):
        collector_with_favorites.delete_book_from_favorites("Гарри Поттер")
        assert "Гарри Поттер" not in collector_with_favorites.get_list_of_favorites_books()

    # Тест 10: Проверка метода get_books_genre
    def test_get_books_genre_method(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}
    
    # Добавляем книгу и проверяем обновленный словарь
        collector.add_new_book("Книга 1")
        assert collector.get_books_genre() == {"Книга 1": ""}
    
    # Устанавливаем жанр и проверяем
        collector.set_book_genre("Книга 1", "Фантастика")
        assert collector.get_books_genre() == {"Книга 1": "Фантастика"}

        # Тест 11: Получение пустого списка избранного
    def test_empty_favorites(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []