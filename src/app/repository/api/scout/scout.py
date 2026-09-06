
import asyncio

import httpx

from app.model.poe import ScoutCurrencyResponse, Item, ScoutItemEntry, ScoutItemResponse
from app.repository.api.constants import LEAGUE, REALM


URL = "https://api.poe2scout.com/poe2/Leagues/runes/Currencies/ByCategory?Category=currency&ReferenceCurrency=exalted&Page=1&PerPage=50&DataPoints=8&FrequencyHours=24"
ITEM_URL = "https://api.poe2scout.com/poe2/Leagues/runes/Items"


URL_PATH : str = "/poe2/Leagues/runes/Currencies/ByCategory"
TRADE_CURRENCY = "exalted"   
INTERVAL = 24

class ScoutRepository():
  BASE_URL : str = "https://api.poe2scout.com"
  def __init__(self):
    self._client = httpx.AsyncClient(
        base_url=self.BASE_URL,
        timeout=httpx.Timeout(10.0,connect=5.0),
        limits=httpx.Limits(max_connections=20, max_keepalive_connections=10)
    )
    self._sem = asyncio.Semaphore(10)
    self.query_string = "History?logCount=100&referenceCurrency=exalted"
    self.scoutCurrencyData: ScoutCurrencyResponse | None

  async def aclose(self) -> None:
        await self._client.aclose()


  async def get_item_price_data(self, id):
    async with self._sem:
       endpoint = "/".join([REALM,"Leagues",LEAGUE,"Items",id, self.query_string])
       return await self._client.get(endpoint)
    
#   async def getPoeScoutOverview(self) -> ScoutCurrencyResponse | None:
#     try:
#         async with aiohttp.ClientSession() as session:
#             async with session.get(URL) as response:
#                 data: ScoutCurrencyResponse = await response.json()
#                 print(data)
#                 return data 
#     except requests.exceptions.HTTPError as error:
#         print(error)
#         return None
    
#   async def getPoeScoutItemOverview(self) -> ScoutItemResponse | None:
#     try:
#         async with aiohttp.ClientSession() as session:
#             async with session.get(ITEM_URL) as response:
#                 data: ScoutItemResponse = await response.json()
#                 print(data)
#                 return data 
#     except requests.exceptions.HTTPError as error:
#         print(error)
#         return None

#     formattedItemData: list[Item] = []
#     for item in data:
#         formattedItem: Item = {
#             "category": item["CategoryApiId"],
#             "description": item["Text"],
#             "name":item["Name"],
#             "item_id":item["ItemId"],
#             "icon_url": item["IconUrl"]
#         }
#         formattedItemData.append(formattedItem)
#     return formattedItemData