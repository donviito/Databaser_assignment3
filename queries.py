from sqlalchemy import func, text
from datetime import date
from db import Session
from models import *

# -------------------------------------------------------
# EXEMPEL – läs detta innan du börjar
# -------------------------------------------------------
#
# RÅ SQL:
#   def example_raw(session):
#       return session.execute(text(
#           "SELECT name FROM librarian ORDER BY name"
#       )).fetchall()
#
# ORM:
#   def example_orm(session):
#       return session.query(Librarian).order_by(Librarian.name).all()
#
# -------------------------------------------------------
# RÅSQL-FRÅGOR  (session.execute + text)
# Returnera alltid resultatet med .fetchall()
# -------------------------------------------------------

def query1(session):
    """
    [RÅ SQL] Hämta alla böcker med titel och utgivningsår.
    Använd: session.execute(text("...")).fetchall()
    """


def query2(session):
    """
    [RÅ SQL] Hämta alla medlemmars namn och e-postadress.
    Använd: session.execute(text("...")).fetchall()
    """
    pass


def query3(session):
    """
    [RÅ SQL] Hämta alla böcker tillsammans med sina författare.
    Varje rad ska innehålla: boktitel, författarnamn.
    Använd: session.execute(text("...")).fetchall()
    """
    pass


def query4(session):
    """
    [RÅ SQL] Hämta namn och medlemsdatum för alla medlemmar
    som gick med efter 2020-12-31.
    Använd: session.execute(text("...")).fetchall()
    """
    pass


def query5(session):
    """
    [RÅ SQL] Hämta namnen på alla medlemmar som har lånat
    minst en bok. Varje namn ska förekomma högst en gång (DISTINCT).
    Använd: session.execute(text("...")).fetchall()
    """
    pass


def query6(session):
    """
    [RÅ SQL] Räkna antalet lån per medlem.
    Varje rad ska innehålla: medlemsnamn, antal lån.
    Använd: session.execute(text("...")).fetchall()
    """
    pass


def query7(session):
    """
    [RÅ SQL] Hämta alla försenade lån, dvs. lån som inte
    återlämnats (return_date IS NULL) och vars förfallodatum
    har passerat dagens datum.
    Varje rad ska innehålla: boktitel, medlemsnamn, förfallodatum.
    Använd: session.execute(text("...")).fetchall()
    """
    pass


# -------------------------------------------------------
# ORM-FRÅGOR  (session.query)
# Observera: dessa använder INTE rå SQL
# -------------------------------------------------------

def query8(session):
    """
    [ORM] Räkna det totala antalet böcker i biblioteket.
    Returnera ett enda heltal, inte en lista.
    Tips: använd func.count() och avsluta med scalar()
    """
    pass


def query9(session):
    """
    [ORM] Hämta det senaste lånet (högst issue_date).
    Returnera ett enda Loan-objekt, inte en lista.
    Tips: använd order_by() och avsluta med first()
    """
    pass


def query10(session):
    """
    [ORM] Hämta alla medlemmar som INTE har lånat någon bok.
    Returnera en lista av Member-objekt.
    Tips: använd outerjoin(), filter() och avsluta med all()
    """
    pass

















# -------------------------------------------------------
# MODELLVALIDERING
# -------------------------------------------------------

def validate_models():
    session = Session()
    errors = []
    try:
        loan = session.query(Loan).first()
        if loan:
            try: _ = loan.member.name
            except AttributeError: errors.append("Loan.member saknas")

            try: _ = loan.copy.book.title
            except AttributeError: errors.append("Loan.copy / BookCopy.book saknas")

            try: _ = loan.librarian.name
            except AttributeError: errors.append("Loan.librarian saknas")

        member = session.query(Member).first()
        if member:
            try: _ = member.loans
            except AttributeError: errors.append("Member.loans saknas")

            try: _ = member.phones
            except AttributeError: errors.append("Member.phones saknas")

        book = session.query(Book).first()
        if book:
            try: _ = book.authors
            except AttributeError: errors.append("Book.authors saknas")

            try: _ = book.genres
            except AttributeError: errors.append("Book.genres saknas")

            try: _ = book.copies
            except AttributeError: errors.append("Book.copies saknas")

        if errors:
            print("\n[MODELLVALIDERING] Följande relationer saknas eller är felaktiga:")
            for e in errors:
                print(f"  ✗ {e}")
        else:
            print("\n[MODELLVALIDERING] Alla relationer OK ✓")
    finally:
        session.close()


# -------------------------------------------------------
# RÄTTNINGSENTRYPOINT – ändra INTE denna funktion
# -------------------------------------------------------

def run_all_queries():
    validate_models()

    session = Session()

    print("\n--- QUERY 1 [SQL]: Alla böcker (titel + utgivningsår) ---")
    print(query1(session))

    print("\n--- QUERY 2 [SQL]: Alla medlemmar (namn + e-post) ---")
    print(query2(session))

    print("\n--- QUERY 3 [SQL]: Böcker med sina författare ---")
    print(query3(session))

    print("\n--- QUERY 4 [SQL]: Medlemmar som gick med efter 2020 ---")
    print(query4(session))

    print("\n--- QUERY 5 [SQL]: Medlemmar som lånat minst en bok ---")
    print(query5(session))

    print("\n--- QUERY 6 [SQL]: Antal lån per medlem ---")
    print(query6(session))

    print("\n--- QUERY 7 [SQL]: Försenade lån ---")
    print(query7(session))

    print("\n--- QUERY 8 [ORM]: Totalt antal böcker ---")
    print(query8(session))

    print("\n--- QUERY 9 [ORM]: Senaste lånet ---")
    print(query9(session))

    print("\n--- QUERY 10 [ORM]: Medlemmar som aldrig lånat ---")
    print(query10(session))

    session.close()


if __name__ == "__main__":
    run_all_queries()
