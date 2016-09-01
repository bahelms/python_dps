from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from dps.models import Base, spec_attribute, specatt

db_conf = "postgres://postgres:postgres@postgres/dps"
engine = create_engine(db_conf, echo=True)

# Check if database exists
try:
    conn = engine.connect()
except Exception as e:
    # Create database if it doesn't exist
    db_conf = "postgres://postgres:postgres@postgres/postgres"
    postgres_engine = create_engine(db_conf, echo=True)
    pg_conn = postgres_engine.connect()
    pg_conn.execute("commit")
    pg_conn.execute("create database dps")
    pg_conn.close()
else:
    conn.close()

# Create source schema
engine.execute("create schema if not exists source").close()

# Create tables
Base.metadata.create_all(engine)

