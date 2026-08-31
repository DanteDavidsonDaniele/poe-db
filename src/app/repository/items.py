from app.model.poe import Item
from app.repository.db import get_conn

ITEMS_DB_NAME: str = "items"

def init_items_db() -> None:
    """Creates the items reference table if it does not already exist"""
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

def insert_item(item:Item):
    with get_conn() as conn:
       conn.execute(f"INSERT INTO {ITEMS_DB_NAME} (item_id, category, name, description, icon_url)  VALUES ('{item.get("item_id")}', '{item.get("category")}', '{item.get("name")}', '{item.get("description")}', '{item.get("icon_url")}');")
       conn.commit()