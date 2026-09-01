from fastapi import APIRouter
from app.repository.items import ItemRepository
from app.service.items import ItemService


class ItemRouter():
    def __init__(self, repository: ItemRepository, service: ItemService):  
       self.repository = repository
       self.service = service
       self.router = APIRouter()

    def _get_all(self):
        @self.router.get("/")
        def get_all():
            items = self.service.get_item_ids()
            return items
        
    def _get_ids(self):
        @self.router.get("/ids")
        def get_ids():
            items = self.service.get_item_ids(["item_id"])
            return items
        
        
    def init_router(self):
        self._get_all()
        self._get_ids()