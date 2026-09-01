import asyncio
from fastapi import APIRouter
from app.repository.trade import TradeRepository
from app.service.constants import TRADE_CURRENCY
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
        
    def _post_single(self):
        @self.router.post("/{item_id}")
        def post_single(item_id: int):
            try:
                item_string_id = str(item_id)
                data =  asyncio.run(self.service.get_item_price_data(item_string_id))
                #print(data)
                if data is None:
                    return None
                items = data["PriceHistory"]
                #print(items)
                for item in items:
                    print()
                    print(item)
                    print()
                    if item is None:
                        continue
                    self.repository.insert(item_string_id, TRADE_CURRENCY, 0, item)
                return items
            except:
                print("unable to add item's price history")
                return None
        
    def init_router(self):
        self._get_all()
        self._post_single()
        # self._get_ids()