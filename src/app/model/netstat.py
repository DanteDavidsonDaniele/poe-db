from typing import TypedDict

class NetstatEntry(TypedDict):           
    protocol: str
    recv_q: int
    send_q:int
    local_address: str
    foreign_address: str
    state: str
    pid: str