"""
created by Nagaj at 05/05/2021
"""
import os

from data.handlejson import JsonMixin


class Book(JsonMixin):
    BOOKS_PATH = os.path.join("data", "books.json")
    PATH = BOOKS_PATH
    books: list = JsonMixin.load_objs(BOOKS_PATH)
    OBJS = books

    def __init__(self, title, pages, author):
        self.title = title
        self.pages = pages
        self.author = author
        self.number_of_bought = 0
        Book.save(self)

    def show_book_details(self):
        print(f"Title: {self.title}")
        print(f"Pages: {self.title}")
        print(f"Author: {self.author}")

    def __repr__(self):
        return self.title

    def get_book_data(self):
        book = {
            "title": self.title,
            "pages": self.pages,
            "author": {
                "username": self.author.username,
                "email": self.author.email,
                "published_books": [repr(book) for book in self.author.published_books],
            },
        }
        return book

    @classmethod
    def save(cls, book):
        # .get_book_data()
        super().save(book)
        print("{} '{}' Was Saved!".format(cls.__name__, book))

    @classmethod
    def to_json(cls):
        cls.OBJS = [
            book.update() if isinstance(book, Book) else book for book in cls.OBJS
        ]
        super().to_json()

    def update(self):
        book = self.get_book_data()
        book.update({"counts": self.number_of_bought})
        return book

    def single_book_to_json(self):
        return {"title": self.title, "pages": self.pages}
