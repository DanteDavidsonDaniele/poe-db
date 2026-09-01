"""Entrypoint. Run with: python -m app.main"""

import asyncio
import logging

from app.config import LOG_LEVEL
from app.model.poe import Item
from app.repository.items import init_items_db, init_price_db
from app.service.poe.economy.scout import handleItemData

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)
log = logging.getLogger(__name__)


def run() -> None:
    init_items_db()
    init_price_db()
    handleItemData()

if __name__ == "__main__":
    run()
