import yaml
from sqlalchemy import create_engine

class DatabaseSupport:
    """Helper class for database operations"""

    def __init__(self, env):
        with open("config/database.yml") as f:
            self.config = yaml.load(f.read())[env]
        db_url = self.db_url_template().format(**self.config)
        self.engine = create_engine(db_url)

    def setup(self):
        self.create_database()
        self.create_source_schema()
        self.create_tables()

    def create_database(self):
        try: # Check if database exists
            conn = self.engine.connect()
        except Exception as e:
            # Create database if it doesn't exist
            db_to_create = self.config["database"]
            self.config["database"] = "postgres"
            db_url = self.db_url_template().format(**self.config)
            postgres_engine = create_engine(db_url, echo=True)
            pg_conn = postgres_engine.connect()
            pg_conn.execute("commit")
            pg_conn.execute("create database {0}".format(db_to_create))
            pg_conn.close()
        else:
            conn.close()

    def create_source_schema(self):
        self.engine.execute("create schema if not exists source").close()

    def create_tables(self):
        from dps.models import Base, spec_attribute, specatt
        Base.metadata.create_all(self.engine)

    def db_url_template(self):
        return "postgres://{username}:{password}@{host}:{port}/{database}"
