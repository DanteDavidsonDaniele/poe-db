"""Entrypoint. Run with: python -m app.main"""

import logging

from app.config import LOG_LEVEL
from app.netstat.index import init_netstat, insert_netstat_entries
from app.ssh.index import get_netstat

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)
log = logging.getLogger(__name__)


def run() -> None:
    netstatEntries = get_netstat()
    init_netstat()
    insert_netstat_entries(netstatEntries)

if __name__ == "__main__":
    run()
