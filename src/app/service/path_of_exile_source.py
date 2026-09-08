from app.repository.api.ggg.ggg import GGGRepository


class POESourceService():
  def __init__(self, source_repository: GGGRepository):
    self.source_repository = source_repository

  async def get_overview(self):
    return "hello world"
  
  async def get_leagues(self):
    return await self.source_repository.get_leagues()
  
  