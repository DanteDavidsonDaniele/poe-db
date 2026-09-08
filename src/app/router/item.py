from fastapi import APIRouter, Depends, Request
from app.router.router import AppRouter
from app.service.items import ItemService

def item_service(request: Request) -> ItemService:
    return request.app.state.item_service

class ItemRouter(AppRouter):
    def __init__(self):  
       super().__init__()
       self._router = APIRouter()
       self._init_routes()

    def _get_all(self):
        @self._router.get("/")
        async def get_all(service:ItemService = Depends(item_service)):
            items = service.get_item_ids()
            return items
        
    def _get_ids(self):
        @self._router.get("/ids")
        async def get_ids(service:ItemService = Depends(item_service)):
            items = service.get_item_ids(["item_id"])
            return items
        
    def _init_routes(self):
        self._get_all()
        self._get_ids()