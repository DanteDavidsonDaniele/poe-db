"""Entrypoint. Run with: python -m app.main"""

import asyncio
import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.config import LOG_LEVEL
from app.model.poe import Item
from app.repository.items import init_items_db, init_price_db
from app.service.poe.economy.scout import handleItemData, handleItemOverview

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)
log = logging.getLogger(__name__)

HOST = "0.0.0.0"
PORT = 8000


def run() -> None:
    init_items_db()
    init_price_db()
    handleItemOverview()
    handleItemData()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Runs once before the server starts accepting requests.
    log.info("Initialising databases and scouting item data...")
    # run() calls asyncio.run() internally, which can't be used inside
    # uvicorn's event loop -- so run it in a worker thread instead.
    await asyncio.to_thread(run)
    log.info("Startup complete, listening on http://%s:%s", HOST, PORT)
    yield
    # Shutdown logic (if any) goes here.


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT, log_level=LOG_LEVEL.lower())