"""
created by Nagaj at 04/05/2021
"""


class Member:
    members = []

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.bought_books = []
        self.favourite_books = []
        Member.members.append(self)

    def show_member_details(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

    def __repr__(self):
        return self.username

    def __getitem__(self, item):
        return Member.members[item]


class User(Member):

    def buy_book(self, book):
        self.bought_books.append(book)

    def show_favourite_books(self, book):
        self.favourite_books.append(book)

    def show_member_details(self):
        super().show_member_details()
        if self.bought_books:
            print(f"Bought Books: {self.bought_books}")
        if self.favourite_books:
            print(f"Favourite Books: {self.favourite_books}")


class Author(User):

    def __init__(self, username, email):
        super(Author, self).__init__(username, email)
        self.published_books = []
        self.reviewed_books = []

    def publish_book(self):
        pass

    def review_book(self):
        pass

    def show_member_details(self):
        super().show_member_details()
        if self.published_books:
            print(f"Published Books: {self.published_books}")

        if self.reviewed_books:
            print(f"Reviewed Books: {self.reviewed_books}")
