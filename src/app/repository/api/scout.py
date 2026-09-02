import requests
import aiohttp

from app.model.poe import ScoutCurrencyResponse, Item, ScoutItemEntry, ScoutItemResponse
from app.repository.api.constants import LEAGUE, REALM


URL = "https://api.poe2scout.com/poe2/Leagues/runes/Currencies/ByCategory?Category=currency&ReferenceCurrency=exalted&Page=1&PerPage=50&DataPoints=8&FrequencyHours=24"
ITEM_URL = "https://api.poe2scout.com/poe2/Leagues/runes/Items"

BASE_URL : str = "https://api.poe2scout.com"
URL_PATH : str = "/poe2/Leagues/runes/Currencies/ByCategory"
TRADE_CURRENCY = "exalted"
INTERVAL = 24

class ScoutRepository():
  def __init__(self):
    self.query_string = "History?logCount=100&referenceCurrency=exalted"
    self.scoutCurrencyData: ScoutCurrencyResponse | None

  async def get_item_price_data(self, id):
    endpoint = "/".join([BASE_URL,REALM,"Leagues",LEAGUE,"Items",id, self.query_string])
    print(endpoint,id)
    try:
        async with aiohttp.ClientSession() as session:
           async with session.get(endpoint) as response:
              data = await response.json()
              print(data)
              return data
    except requests.exceptions.HTTPError as error:
       print(error)
       return None
    
  async def getPoeScoutOverview(self) -> ScoutCurrencyResponse | None:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(URL) as response:
                data: ScoutCurrencyResponse = await response.json()
                print(data)
                return data 
    except requests.exceptions.HTTPError as error:
        print(error)
        return None
    
  async def getPoeScoutItemOverview(self) -> ScoutItemResponse | None:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(ITEM_URL) as response:
                data: ScoutItemResponse = await response.json()
                print(data)
                return data 
    except requests.exceptions.HTTPError as error:
        print(error)
        return None

    formattedItemData: list[Item] = []
    for item in data:
        formattedItem: Item = {
            "category": item["CategoryApiId"],
            "description": item["Text"],
            "name":item["Name"],
            "item_id":item["ItemId"],
            "icon_url": item["IconUrl"]
        }
        formattedItemData.append(formattedItem)
    return formattedItemData