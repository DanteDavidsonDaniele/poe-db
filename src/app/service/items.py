from app.client.ggg import GGGClient
from app.repository.items import ItemRepository

class ItemService():
   def __init__(self, item_repository: ItemRepository, ggg_client:GGGClient):  
       self._item_repository = item_repository
       self._ggg_client = ggg_client

   def get_item_ids(self,fields=["*"]):
       try:
           items = self._item_repository.read(fields)
           return items
       except:
           print("Error")
           return "Unable to get items"
       
   async def get_item_categories(self):
       return await self._ggg_client.get_item_categories()

   async def get_stats(self):
       return await self._ggg_client.get_stats()
