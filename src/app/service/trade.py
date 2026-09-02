import asyncio
from app.model.poe import PriceLogEntry, ScoutCurrencyResponse
from app.repository.api.scout import ScoutRepository
from app.repository.database.items import ItemRepository
from app.repository.database.trade import TradeRepository
from app.repository.api.constants import BASE_URL, LEAGUE, REALM, TRADE_CURRENCY

class TradeService():
  def __init__(self, database_repository:TradeRepository, scout_repository: ScoutRepository, item_database_repository: ItemRepository):
    self.database_repository = database_repository
    self.scout_repository = scout_repository
    self.item_database_repository = item_database_repository
    self._currency = TRADE_CURRENCY

  def get_item_price_data(self, id):
    return asyncio.run(self.scout_repository.get_item_price_data(id))
  
  def get_item_trade_history(self,id:int):
    rows = self.database_repository.read_item(id)
    if rows is None:
      return None
    for row in rows:
      temp = row.column
    return self.database_repository.read_item(id)
  
  def _add_price_data(self,item_id,price_data:PriceLogEntry):
    self.database_repository.insert(item_id,self._currency,0,price_data)
  
  def add_price_data(self):
    rows = self.item_database_repository.read(["item_id"])
    item_prices: list[tuple[str,PriceLogEntry]] = []
    for [index, row] in enumerate(rows):
      item_id = row.stringify_field()
      if  not isinstance(item_id, str):
        continue
      price_data = self.get_item_price_data(item_id)
      if price_data is None:
        continue
      price_history = price_data.get("PriceHistory")
      if price_history is None:
        continue
      for price in price_history:
        if price is None:
          continue
        item_prices.append((item_id,price))
        self.database_repository.insert(item_id,self._currency,0,price)




  
  