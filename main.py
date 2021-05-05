"""
created by Nagaj at 04/05/2021
"""

from accounts.members import Author, User
from books.book import Book


def main():
    user1 = User("user1", "user1@test.com")
    bob = Author("UncleBob", "bob@test.com")
    # author2 = Author("author2", "author2@test.com")
    # author3 = Author("author3", "author3@test.com")
    # author4 = Author("author4", "author4@test.com")
    members = [bob, user1]
    for member in members:
        member.show_member_details()
        print("#" * 100)

    cleancode = Book("CLean Code for software engineers", 400)
    cleanagile = Book("CLean Agile", 500)
    print(cleancode)
    bob.publish_book(cleancode)
    bob.publish_book(cleanagile)
    print(f"Author for {cleancode} is {cleancode.author}")
    print(bob.published_books)
    print(bob.number_of_published_books)


if __name__ == "__main__":
    main()
