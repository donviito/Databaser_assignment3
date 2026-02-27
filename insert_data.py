from db import Session
from models import *
from datetime import date


def seed():
    session = Session()

    # --- Authors ---
    a1  = Author(name="J.K. Rowling",         bio="British author, best known for Harry Potter series.")
    a2  = Author(name="George Orwell",         bio="English novelist, essayist, journalist and critic.")
    a3  = Author(name="J.R.R. Tolkien",        bio="Author of The Lord of the Rings.")
    a4  = Author(name="Agatha Christie",       bio="English writer known for her detective novels.")
    a5  = Author(name="Ernest Hemingway",      bio="American novelist, short-story writer, and journalist.")
    a6  = Author(name="Mark Twain",            bio="American writer, humorist, entrepreneur, and lecturer.")
    a7  = Author(name="Jane Austen",           bio="English novelist known for Pride and Prejudice.")
    a8  = Author(name="F. Scott Fitzgerald",   bio="American novelist best known for The Great Gatsby.")
    a9  = Author(name="Leo Tolstoy",           bio="Russian writer best known for War and Peace.")
    a10 = Author(name="Charles Dickens",       bio="English writer and social critic.")

    # --- Books ---
    b1  = Book(title="Harry Potter and the Sorcerer's Stone", isbn="9780747532699", publication_year=1997)
    b2  = Book(title="1984",                                  isbn="9780451524935", publication_year=1949)
    b3  = Book(title="The Hobbit",                            isbn="9780547928227", publication_year=1937)
    b4  = Book(title="Murder on the Orient Express",          isbn="9780007119318", publication_year=1934)
    b5  = Book(title="The Old Man and The Sea",               isbn="9780684801223", publication_year=1952)
    b6  = Book(title="The Adventures of Huckleberry Finn",    isbn="9780486280615", publication_year=1885)
    b7  = Book(title="Pride and Prejudice",                   isbn="9780141199078", publication_year=1813)
    b8  = Book(title="The Great Gatsby",                      isbn="9780743273565", publication_year=1925)
    b9  = Book(title="War and Peace",                         isbn="9781400079988", publication_year=1869)
    b10 = Book(title="A Tale of Two Cities",                  isbn="9780141439600", publication_year=1859)

    # --- Book–Author ---
    ba1  = BookAuthor(book=b1,  author=a1)
    ba2  = BookAuthor(book=b2,  author=a2)
    ba3  = BookAuthor(book=b3,  author=a3)
    ba4  = BookAuthor(book=b4,  author=a4)
    ba5  = BookAuthor(book=b5,  author=a5)
    ba6  = BookAuthor(book=b6,  author=a6)
    ba7  = BookAuthor(book=b7,  author=a7)
    ba8  = BookAuthor(book=b8,  author=a8)
    ba9  = BookAuthor(book=b9,  author=a9)
    ba10 = BookAuthor(book=b10, author=a10)

    # --- Genres ---
    g1  = BookGenre(book=b1,  genre="Fantasy")
    g2  = BookGenre(book=b2,  genre="Dystopian")
    g3  = BookGenre(book=b3,  genre="Fantasy")
    g4  = BookGenre(book=b4,  genre="Mystery")
    g5  = BookGenre(book=b5,  genre="Fiction")
    g6  = BookGenre(book=b6,  genre="Adventure")
    g7  = BookGenre(book=b7,  genre="Romance")
    g8  = BookGenre(book=b8,  genre="Fiction")
    g9  = BookGenre(book=b9,  genre="Historical Fiction")
    g10 = BookGenre(book=b10, genre="Classic")

    # --- Members ---
    m1  = Member(name="Alice Johnson",  address="123 Maple St",     email="alice@example.com",   membership_date=date(2021, 6, 15))
    m2  = Member(name="Bob Smith",      address="456 Oak Ave",      email="bob@example.com",     membership_date=date(2020, 4, 20))
    m3  = Member(name="Charlie Brown",  address="789 Pine Rd",      email="charlie@example.com", membership_date=date(2019, 8, 10))
    m4  = Member(name="David White",    address="234 Elm St",       email="david@example.com",   membership_date=date(2022, 1, 5))
    m5  = Member(name="Eve Adams",      address="567 Birch Ln",     email="eve@example.com",     membership_date=date(2023, 3, 30))
    m6  = Member(name="Frank Green",    address="890 Cedar Blvd",   email="frank@example.com",   membership_date=date(2021, 12, 25))
    m7  = Member(name="Grace Black",    address="345 Spruce Dr",    email="grace@example.com",   membership_date=date(2020, 7, 15))
    m8  = Member(name="Hank Blue",      address="678 Redwood Ct",   email="hank@example.com",    membership_date=date(2019, 11, 22))
    m9  = Member(name="Ivy Yellow",     address="901 Sequoia Ave",  email="ivy@example.com",     membership_date=date(2022, 9, 10))
    m10 = Member(name="Jack Purple",    address="123 Fir St",       email="jack@example.com",    membership_date=date(2021, 10, 8))

    # --- Phone numbers ---
    p1  = MemberPhone(member=m1,  phone_number="123-456-7890")
    p2  = MemberPhone(member=m2,  phone_number="234-567-8901")
    p3  = MemberPhone(member=m3,  phone_number="345-678-9012")
    p4  = MemberPhone(member=m4,  phone_number="456-789-0123")
    p5  = MemberPhone(member=m5,  phone_number="567-890-1234")
    p6  = MemberPhone(member=m6,  phone_number="678-901-2345")
    p7  = MemberPhone(member=m7,  phone_number="789-012-3456")
    p8  = MemberPhone(member=m8,  phone_number="890-123-4567")
    p9  = MemberPhone(member=m9,  phone_number="901-234-5678")
    p10 = MemberPhone(member=m10, phone_number="012-345-6789")

    # --- Librarians ---
    lib1 = Librarian(name="Librarian One",   email="lib1@example.com")
    lib2 = Librarian(name="Librarian Two",   email="lib2@example.com")
    lib3 = Librarian(name="Librarian Three", email="lib3@example.com")
    lib4 = Librarian(name="Librarian Four",  email="lib4@example.com")
    lib5 = Librarian(name="Librarian Five",  email="lib5@example.com")

    # --- Book copies (one per book) ---
    c1  = BookCopy(book=b1)
    c2  = BookCopy(book=b2)
    c3  = BookCopy(book=b3)
    c4  = BookCopy(book=b4)
    c5  = BookCopy(book=b5)
    c6  = BookCopy(book=b6)
    c7  = BookCopy(book=b7)
    c8  = BookCopy(book=b8)
    c9  = BookCopy(book=b9)
    c10 = BookCopy(book=b10)

    # --- Loans ---
    l1  = Loan(member=m1,  copy=c1,  librarian=lib1, issue_date=date(2024, 1, 10), due_date=date(2024, 2, 10), return_date=None)
    l2  = Loan(member=m2,  copy=c2,  librarian=lib2, issue_date=date(2024, 2, 5),  due_date=date(2024, 3, 5),  return_date=None)
    l3  = Loan(member=m3,  copy=c3,  librarian=lib3, issue_date=date(2024, 1, 20), due_date=date(2024, 2, 20), return_date=date(2024, 2, 18))
    l4  = Loan(member=m4,  copy=c4,  librarian=lib4, issue_date=date(2024, 2, 10), due_date=date(2024, 3, 10), return_date=None)
    l5  = Loan(member=m5,  copy=c5,  librarian=lib5, issue_date=date(2024, 1, 15), due_date=date(2024, 2, 15), return_date=date(2024, 2, 12))
    l6  = Loan(member=m6,  copy=c6,  librarian=lib1, issue_date=date(2024, 2, 1),  due_date=date(2024, 3, 1),  return_date=None)
    l7  = Loan(member=m7,  copy=c7,  librarian=lib2, issue_date=date(2024, 2, 8),  due_date=date(2024, 3, 8),  return_date=None)
    l8  = Loan(member=m8,  copy=c8,  librarian=lib3, issue_date=date(2024, 1, 25), due_date=date(2024, 2, 25), return_date=date(2024, 2, 20))
    l9  = Loan(member=m9,  copy=c9,  librarian=lib4, issue_date=date(2024, 2, 12), due_date=date(2024, 3, 12), return_date=None)
    l10 = Loan(member=m10, copy=c10, librarian=lib5, issue_date=date(2024, 1, 30), due_date=date(2024, 2, 28), return_date=date(2024, 2, 26))

    session.add_all([
        a1, a2, a3, a4, a5, a6, a7, a8, a9, a10,
        b1, b2, b3, b4, b5, b6, b7, b8, b9, b10,
        ba1, ba2, ba3, ba4, ba5, ba6, ba7, ba8, ba9, ba10,
        g1, g2, g3, g4, g5, g6, g7, g8, g9, g10,
        m1, m2, m3, m4, m5, m6, m7, m8, m9, m10,
        p1, p2, p3, p4, p5, p6, p7, p8, p9, p10,
        lib1, lib2, lib3, lib4, lib5,
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10,
        l1, l2, l3, l4, l5, l6, l7, l8, l9, l10,
    ])
    session.commit()
    session.close()

    print("Data inserted.")


if __name__ == "__main__":
    seed()
