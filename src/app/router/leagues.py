from fastapi import APIRouter, Depends, Request
from app.router.router import AppRouter
from app.service.leagues import LeagueService

def league_service(request: Request) -> LeagueService:
    return request.app.state.league_service

class LeagueRouter(AppRouter):
    def __init__(self):  
       super().__init__()
       self._router = APIRouter()
       self._init_routes()

    def _get_all(self):
        @self._router.get("/")
        async def get_all(service:LeagueService = Depends(league_service)):
            return await service.get_leagues()
        
    def _init_routes(self):
        self._get_all()