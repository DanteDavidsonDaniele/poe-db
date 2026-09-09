from app.model.api.ggg.stats import Stat
from app.repository.db import get_conn
from app.repository.db_constants import STAT_DB_NAME
from app.repository.sqlite import Row

class StatsRepository():
    def __init__(self):       # constructor
        with get_conn() as conn:
            conn.executescript(
                f"""
                CREATE TABLE IF NOT EXISTS {STAT_DB_NAME} (
                    id INTEGER PRIMARY KEY,
                    stat_id TEXT UNIQUE NOT NULL,
                    type TEXT NOT NULL,
                    text TEXT NOT NULL   
                );
                """
            )
            conn.commit()

    def read_stats(self):
        try:
            with get_conn() as conn:
                cursor = conn.execute(
                    f"SELECT * FROM {STAT_DB_NAME}"
                )
                rows: list[Row] = cursor.fetchall()
                return rows
        except Exception as error:
            print("Failed to get stats")
            return None

            
    def insert(self, stats: list[Stat]) -> None:
        with get_conn() as conn:
            conn.executemany(
                f"INSERT INTO {STAT_DB_NAME} (stat_id, type, text) "
                "VALUES (?, ?, ?) "
                "ON CONFLICT(stat_id) DO NOTHING;",
                [(stat.id, stat.type, stat.text) for stat in stats],
            )
