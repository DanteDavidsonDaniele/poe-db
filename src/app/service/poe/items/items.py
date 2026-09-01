from app.repository.items import ItemRepository
class ItemService():
   def __init__(self, repository: ItemRepository):  
       self.repository = repository
       self._internal = 0

   def get_item_ids(self):
       try:
           items = self.repository.read(["item_id"])
           print(items)
           return items
       except:
           print("Error")
           return "Unable to get items"

