from sqlite3 import Row
from fastapi import Response
from app.model.poe import PriceLogEntry
from app.client.scout import ScoutClient
from app.repository.items import ItemRepository
from app.repository.trade import TradeRepository
from app.client.constants import TRADE_CURRENCY

class TradeService():
  def __init__(self, trade_repository: TradeRepository, item_repository: ItemRepository, scout_client: ScoutClient):
    self._trade_repository = trade_repository
    self._scout_client = scout_client
    self._item_repository = item_repository
    self._currency = TRADE_CURRENCY
    self._concurrent = 10

  async def get_item_price_data(self, id):
    return await self._scout_client.get_item_price_data(id)
  
  def get_item_trade_history(self,id:int):
    return self._trade_repository.read_item(id)
  
  def _add_price_data(self,item_id, price_data:PriceLogEntry):
    self._trade_repository.insert(item_id,self._currency,0,price_data)

  def _handle_item_row(self, row: Row):
    item_id = row.stringify_field()
    if not item_id == None:
      return self.get_item_price_data(item_id)
    
  def _handle_price_item(self, field: Response):
    price_history = field.get("PriceHistory")

    item_id = field.get("ItemId")
    if price_history is None or item_id is None:
      return None
    for price in price_history:
      if price is None:
        continue
      self._trade_repository.insert(item_id,self._currency,0,price)

  async def add_price_data(self):
    rows = self._item_repository.read(["item_id"])
    row_ids = [row.stringify_field() for row in rows]
    response = await self._scout_client.get_all_item_price_data(row_ids)
    return [self._handle_price_item(field) for field in response]
 