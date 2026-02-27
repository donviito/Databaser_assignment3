from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

"""
Fyll i din egen PostgreSQL-anslutning nedan.
"""

DATABASE_URL = "postgresql+psycopg2://postgres:postgrespw@localhost:5432/Library"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)