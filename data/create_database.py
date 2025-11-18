import os
import time
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from src.database.models import Base

# --- 1. Load Environment Variables ---
# These variables must match those defined in docker-compose.yml
DB_USER = os.getenv("POSTGRES_USER", "aers_user")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "aers_password")
DB_NAME = os.getenv("POSTGRES_DB", "aers_db")
DB_HOST = os.getenv("POSTGRES_HOST", "db")  # IMPORTANT: 'db' is the service name in docker-compose

# Define the connection URL for SQLAlchemy
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

def create_tables(engine):
    """Creates tables using SQLAlchemy ORM metadata."""
    print("-> Attempting to create all tables via SQLAlchemy ORM...")

    # This command inspects all classes derived from Base (User, Item, Interaction)
    # and generates the necessary CREATE TABLE IF NOT EXISTS commands.
    Base.metadata.create_all(engine)

    print("All tables created successfully (via ORM).")


def connect_with_retry(url, retries=5, delay=5):
    """Tries to connect to the database with a delay, essential for Docker Compose startup."""
    for i in range(retries):
        try:
            print(f"Attempting connection to PostgreSQL ({i + 1}/{retries})...")
            # The 'isolation_level="AUTOCOMMIT"' helps manage initial connections
            engine = create_engine(url)
            engine.connect()
            print("Successfully connected to the database!")
            return engine
        except OperationalError as e:
            print(f"Connection failed: {e}")
            if i < retries - 1:
                print(f"Waiting {delay} seconds before retry...")
                time.sleep(delay)
            else:
                print("Failed to connect to the database after all retries.")
                raise e


if __name__ == "__main__":
    # Wait for the DB service to be fully up and running before creating tables
    db_engine = connect_with_retry(DATABASE_URL)

    # Run the table creation
    create_tables(db_engine)