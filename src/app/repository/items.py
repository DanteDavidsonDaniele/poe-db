from app.repository.sqlite import Row
from app.model.poe import Item
from app.repository.db import get_conn
from app.repository.db_constants import ITEMS_DB_NAME


class ItemRepository():
    def __init__(self):
        self._init_db()
    
    @staticmethod
    def _init_db():
        with get_conn() as conn:
            conn.executescript(
                f"""
                PRAGMA foreign_keys = ON;
                CREATE TABLE IF NOT EXISTS {ITEMS_DB_NAME} (
                id INTEGER PRIMARY KEY,
                item_id INTEGER UNIQUE NOT NULL,
                category TEXT NOT NULL,
                name TEXT UNIQUE NOT NULL,
                description TEXT,
                icon_url TEXT
                );
                """
            )

    def insert(self, item:Item):
        with get_conn() as conn:
            conn.execute(
                f"INSERT OR IGNORE INTO {ITEMS_DB_NAME} (item_id, category, name, description, icon_url) "
                "VALUES (?, ?, ?, ?, ?);",
                (
                    item.get("item_id"),
                    item.get("category"),
                    item.get("name"),
                    item.get("description"),
                    item.get("icon_url"),
                ),
                )
            conn.commit()

    def read(self, fields = ["*"]) -> list[Row]:
        query_fields = ", ".join(fields)
        print(query_fields)
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT {query_fields} FROM {ITEMS_DB_NAME}")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            return rows