"""
created by Nagaj at 04/05/2021
"""

from accounts.members import Author, User
from books.book import Book


def main():
    user1 = User("user1", "user1@test.com")
    bob = Author("UncleBob", "bob@test.com")
    john = Author("john", "john@test.com")
    # author2 = Author("author2", "author2@test.com")
    # author3 = Author("author3", "author3@test.com")
    # author4 = Author("author4", "author4@test.com")
    members = [bob, user1]
    for member in members:
        member.show_member_details()
        print("#" * 100)

    cleancode = Book("CLean Code for software engineers", 400, bob)
    cleanagile = Book("CLean Agile", 500, bob)
    python = Book("Python for Pro", 600, john)
    print(cleancode)
    bob.publish_book(cleancode)
    bob.publish_book(cleanagile)
    john.publish_book(python)
    print(f"Author for {cleancode} is {cleancode.author}")
    print(bob.published_books)
    print(bob.number_of_published_books)

    print("#" * 100)
    bob.buy_book(python)
    # john.buy_book(python)

    # print(bob.bought_books)
    # print(john.bought_books)

    print("*" * 100)
    Book.to_json()
    Author.to_json()


if __name__ == "__main__":
    main()
