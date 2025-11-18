#!/bin/sh

export PYTHONPATH=$PYTHONPATH:/app # This allows 'import src.database.models' to work correctly.

echo "Waiting for PostgreSQL to start..."
while ! nc -z db 5432; do
  sleep 1
done
echo "PostgreSQL started and ready!"

echo "Creating database tables..."
python data/create_database.py

exec uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload