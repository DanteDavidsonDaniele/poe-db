from app.client.client import APIClient
from app.model.api.ggg.item_categories import parse_item_categories
from app.model.api.ggg.leagues import parse_leagues
from app.model.api.ggg.stats import parse_stats


class GGGClient(APIClient):
  BASE_URL : str = "https://www.pathofexile.com"
  LEAGUES_PATH : str = "/api/trade2/data/leagues"
  def __init__(self, base_url = BASE_URL):
    super().__init__(base_url)

  async def get_leagues(self):
    async with self._sem:
       response = await self._client.get(self.LEAGUES_PATH)
    response.raise_for_status()
    return parse_leagues(response.json())

  async def get_item_categories(self):
    async with self._sem:
      response = await self._client.get("/api/trade2/data/items")
    response.raise_for_status()
    return parse_item_categories(response.json())

  async def get_stats(self):
    async with self._sem:
      response = await self._client.get("/api/trade2/data/stats")
    response.raise_for_status()
    return parse_stats(response.json())
    
    
