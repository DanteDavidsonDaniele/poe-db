from typing import TypedDict

class Item(TypedDict):
    item_id: int
    name: str
    description: str
    category: str
    icon_url: str

