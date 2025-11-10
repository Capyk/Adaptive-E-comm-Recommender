# KROK 1: Wybór obrazu bazowego
FROM python:3.11-slim

# KROK 2: Ustawienie zmiennych środowiskowych
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Ustawienie katalogu roboczego
WORKDIR /app

# KROK 3: Instalacja zależności systemowych (netcat, narzędzia do budowania)
# netcat jest potrzebny przez entrypoint.sh do czekania na PostgreSQL.
RUN apt-get update \
    && apt-get install -y netcat-openbsd \
    && apt-get install -y build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# KROK 4: Kopiowanie zależności Python i instalacja
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# KROK 5: Kopiowanie skryptu wejściowego i nadanie uprawnień
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# KROK 6: Kopiowanie reszty kodu aplikacji (w tym src/ i data/create_db.py)
COPY . /app/

# KROK 7: Definicja punktu wejścia
# Uruchamia entrypoint.sh, który zarządza kolejnością startu i inicjalizacją DB.
ENTRYPOINT ["/app/entrypoint.sh"]

# KROK 8: Domyślna komenda (przekazywana do entrypoint.sh)
# Gdy skrypt entrypoint.sh zakończy inicjalizację, uruchomi uvicorn.
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]