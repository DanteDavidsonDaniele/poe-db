"""Entrypoint. Run with: python -m app.main"""

import asyncio
import logging

from app.config import LOG_LEVEL
from app.model.poe import Item
from app.repository.items import init_items_db, insert_item
from app.router.netstat import netstat_route
from app.service.poe.economy.scout import getPoeScoutOverview, handleItemData

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)
log = logging.getLogger(__name__)


def run() -> None:
    init_items_db()
    handleItemData()
    # asyncio.run(getPoeScoutOverview())
    # init_items_db()
    # item: Item = {"name":"Mirror of Kalandra","item_id":295,"description":"Right click this item then left click an equipable non-unique item to apply it. Mirrored copies cannot be modified.","category":"currency","icon_url":"https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvQ3VycmVuY3lEdXBsaWNhdGUiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MSwicmVhbG0iOiJwb2UyIn1d/b7f5cc7884/CurrencyDuplicate.png"}
    # insert_item(item)
    # netstat_route()

if __name__ == "__main__":
    run()
