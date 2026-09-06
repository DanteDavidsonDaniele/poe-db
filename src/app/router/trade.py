import asyncio
from fastapi import APIRouter
from app.repository.database.trade import TradeRepository
from app.repository.api.constants import TRADE_CURRENCY
from app.service.items import ItemService
from app.service.trade import TradeService

class TradeRouter():
    def __init__(self, service: TradeService, item_service: ItemService):  
       self.service = service
       self.item_service = item_service
       self.router = APIRouter()
       self._init_router()

    def _get_all(self):
       @self.router.get("/")
       async def get_all():
          items = self.service.get_item_price_data("1")
          return items
       
    def _get_single(self):
       @self.router.get("/{item_id}")
       async def get_single(item_id:int):
          rows = self.service.get_item_trade_history(item_id)
          trade_history = []
          if rows is None:
             return None
          for row in rows:
             trade_history.append(row.column)
          return trade_history

    def _post_all(self):
       @self.router.post("/")
       async def post_all():
          try:
            self.service.add_price_data()
            return "Prices updated"
          except:
            return "Unable to updated prices"
        
    def _init_router(self):
        self._get_all()
        self._get_single()
        self._post_all()
        