"""Entrypoint. Run with: python -m app.main"""

import logging

from app.config import LOG_LEVEL
from app.db import get_conn, init_db

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)
log = logging.getLogger(__name__)


def run() -> None:
    init_db()
    with get_conn() as conn:
        conn.execute("INSERT INTO example (name) VALUES (?)", ("hello world",))
        count = conn.execute("SELECT COUNT(*) AS n FROM example").fetchone()["n"]
    log.info("Rows in example table: %d", count)


if __name__ == "__main__":
    run()
