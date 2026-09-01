from app.model.poe import PriceLogEntry
from app.repository.db import get_conn

ITEMS_DB_NAME: str = "items"
PRICE_DB_NAME: str = "pricing"

def init_price_db() -> None:
    """Creates the item price history table if it does not already exist"""
    with get_conn() as conn:
        conn.executescript(
            f"""
            CREATE TABLE IF NOT EXISTS {PRICE_DB_NAME} (
               id INTEGER PRIMARY KEY,
               item_id INTEGER REFERENCES {ITEMS_DB_NAME}(item_id),
               trade_currency TEXT NOT NULL,
               price INTEGER NOT NULL,
               trade_volume INTEGER NOT NULL,
               trade_timestamp TEXT NOT NULL,
               interval INTEGER NOT NULL,
               UNIQUE(item_id, trade_timestamp)
            );
            """
        )

def insert_price_log(item_id:str, trade_currency:str,interval:int, price_data:PriceLogEntry):
    with get_conn() as conn:
       conn.execute(
        f"INSERT INTO {PRICE_DB_NAME} (item_id, trade_currency, price, trade_volume, trade_timestamp, interval) "
        "VALUES (?, ?, ?, ?, ?, ?) "
        "ON CONFLICT(item_id, trade_timestamp) DO NOTHING;",
        (
            item_id,
            trade_currency,
            price_data.get("Price"),
            price_data.get("Quantity"),
            price_data.get("Time"),
            interval
        ),
        )
       conn.commit()