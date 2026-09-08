import asyncio
from fastapi import APIRouter, Depends, Request
from app.repository.database.trade import TradeRepository
from app.repository.api.constants import TRADE_CURRENCY
from app.router.router import AppRouter
from app.service.items import ItemService
from app.service.trade import TradeService
from app.repository.api.ggg.ggg import GGGRepository
from app.service.path_of_exile_source import POESourceService

def source_service(request:Request) -> POESourceService:
  return request.app.state.source_service

class POESourceRouter(AppRouter):
  def __init__(self):
    self._router = APIRouter()
    self._init_routes()

  def _get_overview(self):
      @self._router.get("/")
      async def get_overview(service:POESourceService= Depends(source_service)):
        return await service.get_overview()
      
  def _init_routes(self):
    self._get_overview()

  

  # def _get_leagues(self):
  #   @self._router.get("/leagues")
  #   async def get_leagues(self):
  #       return await self.source_repository.get_leagues()


    #self._get_leagues()
  