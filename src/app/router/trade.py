from fastapi import APIRouter, Depends, Request
from app.router.router import AppRouter
from app.service.trade import TradeService

def trade_service(request: Request) -> TradeService:
    return request.app.state.trade_service

class TradeRouter(AppRouter):
    def __init__(self):  
       super().__init__()
       self._router = APIRouter()
       self._init_routes()

    def _get_all(self):
       @self._router.get("/")
       async def get_all(service:TradeService = Depends(trade_service)):
          return await service.get_item_price_data("1")
          
       
    def _get_single(self):
       @self._router.get("/{item_id}")
       async def get_single(item_id:int,service:TradeService = Depends(trade_service)):
          rows = service.get_item_trade_history(item_id)
          trade_history = []
          if rows is None:
             return None
          for row in rows:
             trade_history.append(row.column)
          return trade_history

    def _post_all(self):
       @self._router.post("/")
       async def post_all(service:TradeService = Depends(trade_service)):
          try:
            return await service.add_price_data()
          except:
            return "Unable to updated prices"
        
    def _init_routes(self):
        self._get_all()
        self._get_single()
        self._post_all()
        