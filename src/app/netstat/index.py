from typing import TypedDict
from app.db import get_conn

class NetstatEntry(TypedDict):           
    protocol: str
    recv_q: int
    send_q:int
    local_address: str
    foreign_address: str
    state: str
    pid: str

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

def insert_netstat_entries(entries:list[NetstatEntry]):
    with get_conn() as conn:
       cursor = conn.execute(f"INSERT INTO netstat DEFAULT VALUES;")
       table_id = cursor.lastrowid
       for entry in entries:
           conn.executescript(
               f"""
                INSERT INTO netstatEntries (session_id, protocol, recv_q, send_q, local_address, foreign_address, state, pid) VALUES ('{table_id}', '{entry.get("protocol")}', '{entry.get("recv_q")}', '{entry.get("send_q")}', '{entry.get("local_address")}', '{entry.get("foreign_address")}', '{entry.get("state")}', '{entry.get("pid")}');
                """
           )
       conn.commit()