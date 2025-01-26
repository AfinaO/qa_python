from main import BooksCollector
import pytest

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_duplicate(self):
        collector = BooksCollector()

        collector.add_new_book('Дракула')
        collector.add_new_book('Дракула')

        assert len(collector.get_books_genre())

    def test_add_new_book_exceed_max_length(self):
        collector = BooksCollector()

        collector.add_new_book('Г' * 41)

        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Война миров')
        collector.set_book_genre('Война миров', 'Фантастика')

        assert collector.get_book_genre('Война миров') == 'Фантастика'

    def test_get_book_genre_nonexistent(self):
        collector = BooksCollector()

        collector.add_new_book('К себе нежно')

        assert collector.get_book_genre('Неизвестная книга') is None

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Академия')
        collector.set_book_genre('Академия', 'Фантастика')
        collector.add_new_book('Черный телефон')
        collector.set_book_genre('Черный телефон', 'Ужасы')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Академия']

    def test_get_books_genre_returns_dict(self):
        collector = BooksCollector()

        actual_genres = collector.get_books_genre()

        assert isinstance(actual_genres, dict), f"Ожидался словарь, но получен {type(actual_genres).__name__}"

    def test_get_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Питер Пен')
        collector.set_book_genre('Питер Пен', 'Мультфильмы')
        collector.add_new_book('У холмов есть глаза')
        collector.set_book_genre('У холмов есть глаза', 'Ужасы')

        assert collector.get_books_for_children() == ['Питер Пен']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Профайлер')
        collector.set_book_genre('Профайлер', 'Детективы')
        collector.add_book_in_favorites('Профайлер')

        assert collector.get_list_of_favorites_books() == ['Профайлер']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Профайлер')
        collector.set_book_genre('Профайлер', 'Детективы')
        collector.add_book_in_favorites('Профайлер')
        collector.delete_book_from_favorites('Профайлер')

        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_empty(self):
        collector = BooksCollector()

        assert collector.get_list_of_favorites_books() == []

    @pytest.mark.parametrize("book_name, genre", [
        ('Чужой', 'Фантастика'),
        ('Кладбище домашних животных', 'Ужасы'),
        ('Седьмой читатель', 'Детективы'),
    ])
    def test_set_book_genre_for_existing_book(self, book_name, genre):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        assert collector.get_book_genre(book_name) == genre







