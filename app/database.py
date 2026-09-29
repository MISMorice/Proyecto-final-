import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE = BASE_DIR / "data" / "scraper.db"

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    DATABASE.parent.mkdir(exist_ok=True)

    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS scraped_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            url TEXT NOT NULL,
            scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_item(title, url):
    conn = get_connection()

    conn.execute("""
        INSERT INTO scraped_items (title, url)
        VALUES (?, ?)
    """, (title, url))

    conn.commit()
    conn.close()


def get_items():
    conn = get_connection()

    items = conn.execute("""
        SELECT *
        FROM scraped_items
        ORDER BY scraped_at DESC
    """).fetchall()

    conn.close()

    return items
    