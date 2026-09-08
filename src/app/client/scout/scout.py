
import asyncio

import httpx

from app.model.poe import ScoutCurrencyResponse, Item, ScoutItemEntry, ScoutItemResponse
from app.client.client import APIClient
from app.client.constants import LEAGUE, REALM


URL = "https://api.poe2scout.com/poe2/Leagues/runes/Currencies/ByCategory?Category=currency&ReferenceCurrency=exalted&Page=1&PerPage=50&DataPoints=8&FrequencyHours=24"
ITEM_URL = "https://api.poe2scout.com/poe2/Leagues/runes/Items"


URL_PATH : str = "/poe2/Leagues/runes/Currencies/ByCategory"
TRADE_CURRENCY = "exalted"   
INTERVAL = 24

class ScoutClient(APIClient):
  BASE_URL : str = "https://api.poe2scout.com"
  def __init__(self, base_url = BASE_URL):
    super().__init__(base_url)
    self.query_string = "History?logCount=100&referenceCurrency=exalted"
    self.scoutCurrencyData: ScoutCurrencyResponse | None

  async def get_item_price_data(self, id):
    async with self._sem:
       endpoint = "/".join([REALM,"Leagues",LEAGUE,"Items",id, self.query_string])
       response = await self._client.get(endpoint)
       return {**response.json(),"ItemId":id}

  async def get_all_item_price_data(self,ids:list[str]):
      return await asyncio.gather(*(self.get_item_price_data(id) for id in ids))