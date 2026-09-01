import asyncio
from fastapi import APIRouter
from app.repository.trade import TradeRepository
from app.service.trade import TradeService


class TradeRouter():
    def __init__(self, repository: TradeRepository, service: TradeService):  
       self.repository = repository
       self.service = service
       self.router = APIRouter()

    def _get_all(self):
        @self.router.get("/")
        def get_all():
            items = asyncio.run(self.service.get_item_price_data("1"))
            return items
        
    def init_router(self):
        self._get_all()
        # self._get_ids()