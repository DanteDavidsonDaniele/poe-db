import aiohttp
import requests
from app.model.poe import ScoutCurrencyResponse
from app.repository.database.trade import TradeRepository
from app.repository.api.constants import BASE_URL, LEAGUE, REALM

class TradeService():
  def __init__(self, repository:TradeRepository):
    self.repository = repository
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
    
  
  