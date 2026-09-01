"""Entrypoint. Run with: python -m app.main"""
import logging
import uvicorn

from fastapi import FastAPI
from app.config import LOG_LEVEL
from app.repository.items import ItemRepository
from app.repository.trade import  TradeRepository
from app.router.item import ItemRouter
from app.router.trade import TradeRouter
from app.service.items import ItemService
from app.service.trade import TradeService

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)
log = logging.getLogger(__name__)

HOST = "0.0.0.0"
PORT = 8000

# Repositories
item_repository = ItemRepository()
item_repository.init_db()

trade_repository = TradeRepository()

# Services
item_service = ItemService(item_repository)
trade_service = TradeService(trade_repository)

# Routers

item_router = ItemRouter(item_repository,item_service)
item_router.init_router()

trade_router = TradeRouter(trade_repository,trade_service)
trade_router.init_router()

app = FastAPI()
app.include_router(item_router.router,prefix="/items")
app.include_router(trade_router.router,prefix="/trade")


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT, log_level=LOG_LEVEL.lower())