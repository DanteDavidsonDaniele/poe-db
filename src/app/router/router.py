from abc import abstractmethod
from typing import Protocol
from fastapi import APIRouter


class AppRouter(Protocol):
    _router:APIRouter

    @abstractmethod
    def _init_routes(self):
        raise NotImplementedError