"""
created by Nagaj at 05/05/2021
"""


class Book:

    def __init__(self, title, pages, author=None):
        self.title = title
        self.pages = pages
        self.author = author

    def show_book_details(self):
        print(f"Title: {self.title}")
        print(f"Pages: {self.title}")
        print(f"Author: {self.author}")

    def __repr__(self):
        return self.title
