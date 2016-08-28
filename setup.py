from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
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

# Create tables
metadata = MetaData()
hspecatt = Table("hspecatt", metadata,
    Column("id", Integer, primary_key=True),
    Column("hadlcd", String),
    Column("hadiv", String),
    Column("haspec", String),
    Column("hadesc", String)
)

metadata.create_all(engine)

