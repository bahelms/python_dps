import os
from database_support import DatabaseSupport

env = os.environ.get("DPS_ENV", default="development")
DatabaseSupport(env).setup()
