import asyncio
from sqlite3 import Row

from fastapi import Response
from app.model.poe import PriceLogEntry
from app.client.scout.scout import ScoutClient
from app.repository.database.items import ItemRepository
from app.repository.database.trade import TradeRepository
from app.client.constants import BASE_URL, LEAGUE, REALM, TRADE_CURRENCY

class TradeService():
  def __init__(self, database_repository:TradeRepository, scout_repository: ScoutClient, item_database_repository: ItemRepository):
    self.database_repository = database_repository
    self.scout_repository = scout_repository
    self.item_database_repository = item_database_repository
    self._currency = TRADE_CURRENCY
    self._concurrent = 10

  async def get_item_price_data(self, id):

    return await self.scout_repository.get_item_price_data(id)
  
  def get_item_trade_history(self,id:int):
    return self.database_repository.read_item(id)
  
  def _add_price_data(self,item_id, price_data:PriceLogEntry):
    self.database_repository.insert(item_id,self._currency,0,price_data)

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
      self.database_repository.insert(item_id,self._currency,0,price)

  async def add_price_data(self):
    rows = self.item_database_repository.read(["item_id"])
    row_ids = [row.stringify_field() for row in rows]
    response = await self.scout_repository.get_all_item_price_data(row_ids)
    return [self._handle_price_item(field) for field in response]
 