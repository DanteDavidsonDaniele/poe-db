"""Entrypoint. Run with: python -m app.main"""

import logging

from app.config import LOG_LEVEL
from app.router.netstat import netstat_route

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)
log = logging.getLogger(__name__)


def run() -> None:
    netstat_route()

if __name__ == "__main__":
    run()
