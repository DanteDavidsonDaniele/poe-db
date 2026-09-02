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

    def _get_all(self):
       @self.router.get("/")
       def get_all():
          #self.service.add_price_data()
          items = self.service.get_item_price_data("1")
          return items
    def _get_single(self):
       @self.router.get("/{item_id}")
       def get_single(item_id:int):
          print(item_id)
          rows = self.service.get_item_trade_history(item_id)
          trade_history = []
          if rows is None:
             return None
          for row in rows:
             trade_history.append(row.column)
          return trade_history
        
    def init_router(self):
        self._get_all()
        self._get_single()
        
    # def _post_single(self):
    #     @self.router.post("/{item_id}")
    #     def post_single(item_id: int):
    #         try:
    #             item_string_id = str(item_id)
    #             data =  self.service.get_item_price_data(item_string_id)
    #             if data is None:
    #                 return None
    #             items = data["PriceHistory"]
    #             for item in items:
    #                 print()
    #                 print(item)
    #                 print()
    #                 if item is None:
    #                     continue
    #                 self.repository.insert(item_string_id, TRADE_CURRENCY, 0, item)
    #             return items
    #         except:
    #             print("unable to add item's price history")
    #             return None

        
   
        #self._post_single()