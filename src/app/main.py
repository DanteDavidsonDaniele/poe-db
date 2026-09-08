"""Entrypoint. Run with: python -m app.main"""
import asyncio
import logging
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.config import LOG_LEVEL

from app.repository.items import ItemRepository
from app.repository.trade import  TradeRepository
from app.client.scout.scout import  ScoutClient
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

# # Repositories
# item_repository = ItemRepository()
# item_repository.init_db()


# scout_repository = ScoutRepository()

# ggg_repository = GGGRepository()

# # Services
# item_service = ItemService(item_repository)
# # trade_service = TradeService(trade_repository, scout_repository, item_repository)
# source_service = POESourceService(ggg_repository)

# # Routers

item_router = ItemRouter()
trade_router = TradeRouter()

@asynccontextmanager
async def lifespan(app: FastAPI):

    item_repository = ItemRepository()
    trade_repository = TradeRepository()

    scout_repository = ScoutClient()

    app.state.item_service = ItemService(item_repository)
    app.state.trade_service = TradeService(trade_repository, scout_repository, item_repository)

    closeable = (scout_repository,)

    yield

    await asyncio.gather(*(r.aclose() for r in closeable), return_exceptions=True)


app = FastAPI(lifespan=lifespan)
app.include_router(item_router._router,prefix="/items")
app.include_router(trade_router._router,prefix="/trade")


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT, log_level=LOG_LEVEL.lower())