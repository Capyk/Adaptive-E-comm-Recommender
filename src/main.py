# src/main.py

from fastapi import FastAPI
import os

app = FastAPI(
    title="AERS - Adaptive E-commerce Recommendation System",
    version="1.0.0"
)

# Optional: Print credentials on startup to confirm they are loaded
DB_HOST = os.getenv("POSTGRES_HOST")
print(f"Attempting to connect to DB at: {DB_HOST}")


@app.get("/")
def read_root():
    """
    Prosty endpoint testowy dla weryfikacji, czy API jest aktywne.
    """
    return {"message": "AERS API Running"}

@app.get("/health")
def health_check():
    """
    Basic health check for the application (Liveness).
    A more advanced check would verify the DB connection.
    """
    return {"status": "ok", "service": "AERS API"}


# You will add database connection setup here later
# ...