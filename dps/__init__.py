import yaml
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_conf = "postgres://postgres:postgres@postgres/dps"
engine  = create_engine(db_conf, echo=True)
Session = sessionmaker(bind=engine)

