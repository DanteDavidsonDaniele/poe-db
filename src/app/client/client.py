import asyncio
import httpx

HEADERS = {
    "User-Agent": "OAuth network_data/1.0 (contact: you@gmail.com)",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
}

class APIClient:
    def __init__(self, base_url) -> None:
        self._client = httpx.AsyncClient(
            base_url=base_url,
            headers=HEADERS,
            timeout=httpx.Timeout(10.0, connect=5.0),
            limits=httpx.Limits(max_connections=100, max_keepalive_connections=20),
        )
        self._sem = asyncio.Semaphore(10)

    async def aclose(self) -> None:
        await self.async_client.aclose()
