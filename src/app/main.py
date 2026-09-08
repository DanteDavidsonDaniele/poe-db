# Libs
import asyncio
import logging
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI

# Config
from app.config import LOG_LEVEL

# Repositories
from app.repository.items import ItemRepository
from app.repository.trade import  TradeRepository

# Clients
from app.client.scout import  ScoutClient
from app.client.ggg import GGGClient

# Routers
from app.router.item import ItemRouter
from app.router.leagues import LeagueRouter
from app.router.trade import TradeRouter

# Services
from app.service.items import ItemService
from app.service.leagues import LeagueService
from app.service.trade import TradeService

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)
log = logging.getLogger(__name__)

HOST = "0.0.0.0"
PORT = 8000

# Initialise Routers
item_router = ItemRouter()
league_router = LeagueRouter()
trade_router = TradeRouter()

@asynccontextmanager
async def lifespan(app: FastAPI):

    # Initialise Repositories
    item_repository = ItemRepository()
    trade_repository = TradeRepository()


    # Initialise Clients
    ggg_client = GGGClient()
    scout_client = ScoutClient()

    # Initialise Services
    app.state.item_service = ItemService(item_repository,ggg_client)
    app.state.league_service = LeagueService(ggg_client)
    app.state.trade_service = TradeService(trade_repository, scout_client, item_repository)

    closeable = (scout_client,ggg_client,)

    yield

    await asyncio.gather(*(r.aclose() for r in closeable), return_exceptions=True)


app = FastAPI(lifespan=lifespan)
app.include_router(item_router._router,prefix="/items")
app.include_router(league_router._router,prefix="/leagues")
app.include_router(trade_router._router,prefix="/trade")


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT, log_level=LOG_LEVEL.lower())