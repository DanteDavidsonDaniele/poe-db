from app.model.poe import PriceLogEntry
from app.repository.db import get_conn
from app.repository.db_constants import ITEMS_DB_NAME, TRADE_DB_NAME

class TradeRepository():
    def __init__(self):       # constructor
        with get_conn() as conn:
            conn.executescript(
                f"""
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
            
    def insert(self,item_id:str, trade_currency:str,interval:int, price_data:PriceLogEntry):
        with get_conn() as conn:
            conn.execute(
                f"INSERT INTO {TRADE_DB_NAME} (item_id, trade_currency, price, trade_volume, trade_timestamp, interval) "
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
