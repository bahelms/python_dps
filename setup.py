import yaml
import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from dps.models import Base, spec_attribute, specatt

env = os.environ.get("DPS_ENV", default="development")

with open("config/database.yml") as f:
    config = yaml.load(f.read())[env]

db_conn_template = "postgres://{username}:{password}@{host}:{port}/{database}"
db_conn = db_conn_template.format(**config)
engine = create_engine(db_conn, echo=True)

# Check if database exists
try:
    conn = engine.connect()
except Exception as e:
    # Create database if it doesn't exist
    config["database"] = "postgres"
    db_conn = db_conn_template.format(**config)
    postgres_engine = create_engine(db_conn, echo=True)
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

