import asyncio
import httpx

class APIClient:
    def __init__(self, base_url) -> None:
        self._client = httpx.AsyncClient(
            base_url=base_url,
            timeout=httpx.Timeout(10.0, connect=5.0),
            limits=httpx.Limits(max_connections=100, max_keepalive_connections=20),
        )
        self._sem = asyncio.Semaphore(10)

    async def aclose(self) -> None:
        await self.async_client.aclose()
