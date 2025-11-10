#!/bin/sh

# 1. Czekanie na gotowość PostgreSQL (Klucz MLOps)
# To jest kluczowe, aby uniknąć błędów połączenia na starcie.
echo "Waiting for PostgreSQL to start..."
# Sprawdza, czy port 5432 na hoście 'db' jest otwarty (czyli czy Postgres działa)
while ! nc -z db 5432; do
  sleep 1
done
echo "PostgreSQL started and ready!"

# 2. Inicjalizacja Bazy Danych
# Uruchom skrypt tworzenia tabel.
# Jeśli tabele już istnieją, skrypt powinien zadziałać bez błędów (CREATE TABLE IF NOT EXISTS).
echo "Creating database tables..."
python data/create_db.py

exec uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload