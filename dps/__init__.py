import yaml
import os
from database_support import DatabaseSupport
from sqlalchemy.orm import sessionmaker

env = os.environ.get("DPS_ENV", default="development")
db = DatabaseSupport(env)
Session = sessionmaker(bind=db.engine)

with open("config/config.yml") as f:
    config = yaml.load(f.read())
