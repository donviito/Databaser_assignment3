from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    bio = Column(Text)

    # TODO: lägg till relationship till BookAuthor (back_populates="author")


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    isbn = Column(String(20), unique=True, nullable=False)
    publication_year = Column(Integer)

    # TODO: lägg till relationship till BookAuthor (back_populates="book")
    # TODO: lägg till relationship till BookGenre  (back_populates="book")
    # TODO: lägg till relationship till BookCopy   (back_populates="book")


class BookAuthor(Base):
    __tablename__ = "book_author"

    book_id   = Column(Integer, ForeignKey("book.id"),   primary_key=True)
    author_id = Column(Integer, ForeignKey("author.id"), primary_key=True)

    book   = relationship("Book",   back_populates="authors")
    author = relationship("Author", back_populates="books")


class BookGenre(Base):
    __tablename__ = "book_genre"

    book_id = Column(Integer, ForeignKey("book.id"), primary_key=True)
    genre   = Column(String(100), primary_key=True)

    # TODO: lägg till relationship till Book (back_populates="genres")


class Member(Base):
    __tablename__ = "member"

    id              = Column(Integer, primary_key=True)
    name            = Column(String(255), nullable=False)
    address         = Column(Text, nullable=False)
    email           = Column(String(255), unique=True, nullable=False)
    membership_date = Column(Date, nullable=False)

    # TODO: lägg till relationship till MemberPhone (back_populates="member")
    # TODO: lägg till relationship till Loan        (back_populates="member")

    def __repr__(self):
        return f"<Member id={self.id} name={self.name!r} email={self.email!r}>"


class MemberPhone(Base):
    __tablename__ = "member_phone"

    member_id    = Column(Integer, ForeignKey("member.id"), primary_key=True)
    phone_number = Column(String(20), primary_key=True)

    # TODO: lägg till relationship till Member (back_populates="phones")


class Librarian(Base):
    __tablename__ = "librarian"

    id    = Column(Integer, primary_key=True)
    name  = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)

    # TODO: lägg till relationship till Loan (back_populates="librarian")


class BookCopy(Base):
    __tablename__ = "book_copy"

    id      = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("book.id"), nullable=False)

    # TODO: lägg till relationship till Book (back_populates="copies")
    # TODO: lägg till relationship till Loan (back_populates="copy")


class Loan(Base):
    __tablename__ = "loan"

    id           = Column(Integer, primary_key=True)
    member_id    = Column(Integer, ForeignKey("member.id"),    nullable=False)
    copy_id      = Column(Integer, ForeignKey("book_copy.id"), nullable=False)
    librarian_id = Column(Integer, ForeignKey("librarian.id"), nullable=False)
    issue_date   = Column(Date, nullable=False)
    due_date     = Column(Date, nullable=False)
    return_date  = Column(Date)

    # TODO: lägg till relationship till Member    (back_populates="loans")
    # TODO: lägg till relationship till BookCopy  (back_populates="loans")
    # TODO: lägg till relationship till Librarian (back_populates="loans")

    def __repr__(self):
        return f"<Loan id={self.id} member_id={self.member_id} issue_date={self.issue_date} due_date={self.due_date} return_date={self.return_date}>"
