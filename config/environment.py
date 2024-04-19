import os

db_URI = os.getenv("DATABASE_URL", "postgresql://localhost:5432/groups_db")
SECRET = os.getenv("SECRET", "umbrellagrandioseboatlimelibrary")

if db_URI.startswith("postgres://"):
    db_URI = db_URI.replace("postgres://", "postgresql://", 1)
