from app.model.poe import PriceLogEntry
from app.repository.database.db import get_conn
from app.repository.database.db_constants import ITEMS_DB_NAME, TRADE_DB_NAME
from app.repository.database.sqlite import Row

class TradeRepository():
    def __init__(self):       # constructor
        with get_conn() as conn:
            conn.executescript(
                f"""
                CREATE TABLE IF NOT EXISTS {TRADE_DB_NAME} (
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
            conn.commit()

    def read_item(self, item_id: int):
        try:
            with get_conn() as conn:
                cursor = conn.execute(
                    f"SELECT * FROM {TRADE_DB_NAME} WHERE item_id = ?",
                    (item_id,)
                )
                rows: list[Row] = cursor.fetchall()
                return rows
        except Exception as error:
            print("Failed to get items")
            return None

            
    def insert(self,item_id:str, trade_currency:str,interval:int, price_data:PriceLogEntry):
        try:
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
                return [f"Item {item_id} added to table.", None]
            
        except Exception as error:    
            print()
            print("Unable to handle error:")
            print(error)
            print() 
            return [None, "Database"]
