import aiohttp
import requests
from app.model.poe import ScoutCurrencyResponse
from app.repository.trade import TradeRepository

class TradeService():
  def __init__(self, repository:TradeRepository):
    self.repository = repository
    self.url = "https://api.poe2scout.com/poe2/Leagues/runes/Items/486/History?logCount=100&referenceCurrency=exalted"
    self.scoutCurrencyData: ScoutCurrencyResponse | None

  async def get_item_price_data(self, id):
    try:
        async with aiohttp.ClientSession() as session:
           async with session.get(self.url) as response:
              data = await response.json()
              print(data)
              return data
    except requests.exceptions.HTTPError as error:
       print(error)
       return None
  