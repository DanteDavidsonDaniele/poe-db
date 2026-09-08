from app.client.ggg import GGGClient

class LeagueService():
   def __init__(self, client: GGGClient):  
       self._client = client

   async def get_leagues(self):
       return await self._client.get_leagues()
