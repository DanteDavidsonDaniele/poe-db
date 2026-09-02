"""SQLite helpers. Stdlib only - no ORM needed at this stage."""

import sqlite3
from contextlib import contextmanager
from app.config import DB_PATH


@contextmanager
def get_conn():
    """Yield a connection that commits on success and rolls back on error."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row 
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


