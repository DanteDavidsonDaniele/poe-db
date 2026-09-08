from app.client.client import APIClient
from app.model.api.ggg import League, parse_leagues


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
    
