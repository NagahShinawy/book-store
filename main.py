"""
created by Nagaj at 04/05/2021
"""

from accounts.members import Author, User


def main():
    user1 = Author("user1", "user1@test.com")
    bob = Author("UncleBob", "bob@test.com")
    author2 = Author("author2", "author2@test.com")
    author3 = Author("author3", "author3@test.com")
    author4 = Author("author4", "author4@test.com")
    members = [author4, bob, author3, author2, user1]
    for member in members:
        print(member)


if __name__ == "__main__":
    main()
