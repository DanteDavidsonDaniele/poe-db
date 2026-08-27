
from app.db import get_conn
def init_netstat() -> None:
    """Create tables if they don't exist. Extend this as your schema grows."""
    dbName:str = "netstat"
    with get_conn() as conn:
        conn.executescript(
            f"""
            PRAGMA foreign_keys = ON;
            CREATE TABLE IF NOT EXISTS {dbName} (
               id INTEGER PRIMARY KEY,
               created_at TEXT NOT NULL DEFAULT (datetime('now'))
            );
            CREATE TABLE IF NOT EXISTS {dbName}Entries (
                id INTEGER PRIMARY KEY,
                session_id INTEGER REFERENCES {dbName}(id),
                protocol TEXT NOT NULL,
                recv_q INTEGER NOT NULL,
                send_q INTEGER NOT NULL,
                local_address TEXT NOT NULL,
                foreign_address TEXT NOT NULL,
                state TEXT,
                pid TEXT,
                created_at TEXT NOT NULL DEFAULT (datetime('now'))
            );
            """
        )

#         from app.db import get_conn

# def init_netstat() -> None:
#     """Create tables if they don't exist. Extend this as your schema grows."""
#     dbName:str = "netstat"
#     with get_conn() as conn:
#         conn.executescript(
#             f"""
#             CREATE TABLE IF NOT EXISTS {dbName} (
#                 id INTEGER PRIMARY KEY,
#                 created_at TEXT NOT NULL DEFAULT (datetime('now'))
#             );
#             CREATE TABLE IF NOT EXISTS {dbName}_entries (
#                 id INTEGER PRIMARY KEY,
#                 session_id INTEGER NOT NULL,
#                 protocol TEXT NOT NULL,
#                 recv_q INTEGER NOT NULL,
#                 send_q INTEGER NOT NULL,
#                 local_address TEXT NOT NULL,
#                 foreign_address TEXT NOT NULL,
#                 state TEXT,
#                 pid TEXT,
#                 created_at TEXT NOT NULL DEFAULT (datetime('now')),
#                 FOREIGN KEY (session_id)
#             );
#             """
#         )