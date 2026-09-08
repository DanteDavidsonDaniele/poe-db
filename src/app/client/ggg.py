from app.repository.api.api import APIClient


class GGGClient(APIClient):
  BASE_URL : str = "https://www.pathofexile.com"
  LEAGUES_PATH : str = "/api/trade2/data/leagues"
  def __init__(self, base_url = BASE_URL):
    super().__init__(base_url)

  async def get_leagues(self):
    async with self._sem:
       return await self._client.get(self.LEAGUES_PATH)
    
