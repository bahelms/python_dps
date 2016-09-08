# Data Processing System
Monitors a directory for CSV files and processes anything it finds.

### Development Setup

    docker-compose build
    docker-compose up

### Todo
* Have tests use their own test database
* Unique constraint violation: Everything is an insert; updates aren't automatic
* Convert delete code into deleted_at timestamp
* Move table creation into Alembic migrations
* Move database config in setup.py into config file
* Dynamically add model columns from config
