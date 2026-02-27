# Databaser 2026 – Inlämningsuppgift 3 



## Databasschema – Library

Vi använder följande tabeller:

```
Author       (id, name, bio)
Book         (id, title, isbn, publication_year)
Book_Author  (book_id, author_id)                                    -- kopplingstabell
Book_Genre   (book_id, genre)                                        -- kopplingstabell
Member       (id, name, address, email, membership_date)
Member_Phone (member_id, phone_number)                               -- multivärdat attribut
Librarian    (id, name, email)
Book_Copy    (id, book_id)                                           -- fysiska exemplar
Loan         (id, member_id, copy_id, librarian_id, issue_date, due_date, return_date)
```

---

# ORM (Python + SQLAlchemy)

## Repo-struktur

```
Databaser_assignment3/
├── db.py           ← anslutning (du fyller i)
├── models.py       ← ORM-modeller (du kompletterar)
├── create_db.py    ← skapar tabeller
├── insert_data.py  ← fyller i testdata
├── queries.py      ← dina 10 frågor (du implementerar)
└── requirements.txt
```

## Förutsättningar

- Python 3.8+
- PostgreSQL installerat och igång (t.ex. via pgAdmin)

## Steg 0 – Klona repot

```
git clone https://github.com/donviito/Databaser_assignment3.git
cd Databaser_assignment3
```

## Steg 1 – Skapa databasen

Skapa en tom PostgreSQL-databas med namnet `Library` i pgAdmin. Skapa inga tabeller manuellt.

## Steg 2 – Skapa virtuell miljö och installera beroenden

Skapa en virtuell miljö för att undvika konflikter med systemets Python-paket:

```
python -m venv venv
```

Aktivera miljön:

```
# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

Installera sedan beroenden:

```
pip install -r requirements.txt
```

> Du behöver aktivera `venv` varje gång du öppnar en ny terminal för det här projektet.

## Steg 3 – Konfigurera anslutning

Öppna `db.py` och ersätt `username` och `password` med dina PostgreSQL-uppgifter:

```
postgresql+psycopg2://username:password@localhost:5432/Library
```

## Steg 4 – Komplettera modellerna

Öppna `models.py`. Kolumndefinitioner är givna för alla tabeller. Din uppgift är att lägga till de
`relationship()`-deklarationer som saknas (markerade med `# TODO` i filen). `BookAuthor` är
färdigimplementerad och visar hur det ska se ut.

## Steg 5 – Skapa tabeller via kod

När modellerna är klara kör du:

```
python create_db.py
```

Detta anropar `Base.metadata.create_all(engine)` och skapar samtliga tabeller i databasen automatiskt.
Inga tabeller ska skapas manuellt i pgAdmin.

## Steg 6 – Fyll i testdata via kod

```
python insert_data.py
```

Detta kör en seed-funktion som lägger in 10 böcker, 10 författare, 10 medlemmar,
5 bibliotekarier, 10 bokexemplar och 10 lån. All data hanteras via ORM-sessionen.

## Steg 7 – Implementera frågor

Du ska implementera 10 frågor i `queries.py`, uppdelade i två kategorier:

**Rå-SQL (7 frågor):** Skriv en vanlig SQL-sträng och kör den via SQLAlchemy-sessionen:
```python
result = session.execute(text("SELECT ..."))
return result.fetchall()
```

**ORM (3 frågor):** Använd `session.query(...)` utan rå SQL. Varje ORM-fråga
använder en specifik returmetod – läs docstringen noggrant.

Kör alla frågor:

```
python queries.py
```

`run_all_queries()` används vid rättning – **ändra inte den funktionen**.

## Frågor

| # | Typ | Beskrivning | Returnerar |
|---|---|---|---|
| 1 | Rå SQL | Alla böcker med titel och utgivningsår | `fetchall()` |
| 2 | Rå SQL | Alla medlemmars namn och e-post | `fetchall()` |
| 3 | Rå SQL | Alla böcker med sina författare (JOIN) | `fetchall()` |
| 4 | Rå SQL | Medlemmar som gick med efter 2020 | `fetchall()` |
| 5 | Rå SQL | Medlemmar som lånat minst en bok (DISTINCT) | `fetchall()` |
| 6 | Rå SQL | Antal lån per medlem (GROUP BY) | `fetchall()` |
| 7 | Rå SQL | Försenade lån – titel, namn, förfallodatum | `fetchall()` |
| 8 | ORM | Totalt antal böcker (COUNT) | `.scalar()` |
| 9 | ORM | Senaste lånet (ORDER BY + first) | `.first()` |
| 10 | ORM | Medlemmar som aldrig lånat (outerjoin + NULL) | `.all()` |

## Inlämning

Lämna in:
- `models.py`
- `queries.py`

Lösningen ska kunna köras utan ändringar efter att `create_db.py` och `insert_data.py` körts mot databasen `Library`.

Rättning sker via `run_all_queries()` i `queries.py` – **ändra inte den funktionen**.

## Bedömning

- Korrekta `relationship()`-relationer med `back_populates` i `models.py`
- Rå-SQL-frågor returnerar korrekt data via `session.execute(text(...))`
- ORM-frågor använder rätt metod (`.scalar()`, `.first()`, `.all()`)
- Korrekt JOIN-logik, filtrering och aggregation
- Kodens läsbarhet och struktur
