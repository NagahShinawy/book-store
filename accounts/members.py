"""
created by Nagaj at 04/05/2021
"""
import os

from books.book import Book
from data.handlejson import JsonMixin


class Member(JsonMixin):
    MEMBERS_PATH = os.path.join("data", "members.json")
    PATH = MEMBERS_PATH
    members: list = JsonMixin.load_objs(MEMBERS_PATH)
    objs = members

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.bought_books = []
        self.favourite_books = []
        Member.save(self)

    @classmethod
    def save(cls, member):
        super().save(member)
        print(f"{cls.__name__}  {member} was saved")

    @classmethod
    def to_json(cls):
        cls.objs = [
            member.get_member_data() if not isinstance(member, dict) else member
            for member in cls.objs
        ]
        super().to_json()

    def get_member_data(self):
        member_data = {
            "username": self.username,
            "email": self.email,
            "fav_books": [book.single_book_to_json() for book in self.favourite_books],
            "bought_books": [book.single_book_to_json() for book in self.bought_books],
        }
        if isinstance(self, Author):
            member_data.update(
                {
                    "published_books": [
                        book.single_book_to_json() for book in self.published_books
                    ]
                }
            )
        return member_data

    def show_member_details(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

    def __repr__(self):
        return self.username

    def __getitem__(self, item):
        return Member.members[item]


class User(Member):
    def __init__(self, username, email):
        super().__init__(username, email)

    def buy_book(self, book: Book):
        self.bought_books.append(book)
        book.number_of_bought += 1
        print(
            "Thanks '{}' for buying our book '{}'. I hope you enjoy".format(self, book)
        )

    def add_book_to_favourite(self, book: Book):
        self.favourite_books.append(book)

    def show_member_details(self):
        super().show_member_details()
        if self.bought_books:
            print(f"Bought Books: {self.bought_books}")
        if self.favourite_books:
            print(f"Favourite Books: {self.favourite_books}")

    def list_bought_books(self):
        books = self.bought_books
        if books:
            for book in books:
                print(book)
        else:
            print("No Bought Books to show")

    def list_favourite_books(self):
        books = self.favourite_books
        if not books:
            print("No Favourite Books")
        else:
            for book in books:
                print(book)


class Author(User):
    def __init__(self, username, email):
        super(Author, self).__init__(username, email)
        self.published_books = []
        self.reviewed_books = []

    def publish_book(self, book: Book):
        self.published_books.append(book)
        print(f"book: {book} was published successfully")

    def review_book(self, book: Book):
        self.reviewed_books.append(book)

    def show_member_details(self):
        super().show_member_details()
        if self.published_books:
            print(f"Published Books: {self.published_books}")

        if self.reviewed_books:
            print(f"Reviewed Books: {self.reviewed_books}")

    @property
    def number_of_published_books(self):
        return len(self.published_books)

    @property
    def number_of_reviewed_books(self):
        return len(self.reviewed_books)
