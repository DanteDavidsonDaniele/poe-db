"""Entrypoint. Run with: python -m app.main"""
import logging
import uvicorn

from fastapi import FastAPI
from app.config import LOG_LEVEL
from app.repository.items import init_items_db
from app.repository.currency import  init_price_db
from app.service.poe.items.items import handle_item_overview

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)
log = logging.getLogger(__name__)

HOST = "0.0.0.0"
PORT = 8000

app = FastAPI()

@app.get("/")
def read_root():
    init_items_db()
    init_price_db()
    return {"Hello": "World"}


@app.get("/items")
def read_item():
    items = handle_item_overview()
    return {"response":items}


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT, log_level=LOG_LEVEL.lower())