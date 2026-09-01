from typing import NotRequired, TypedDict


class PriceLogEntry(TypedDict):
    Price: int
    Time: str
    Quantity: int

class Item(TypedDict):
    item_id: int
    name: str
    description: str
    category: str
    icon_url: str
    price_data: NotRequired[list[PriceLogEntry]]

class CurrencyItemMetadata(TypedDict):
    name: str
    base_type: str
    icon: str
    stack_size: int
    max_stack_size: int
    description: str
    effect: list[str]

class ScoutCurrencyEntry(TypedDict):
    CurrencyItemId: int
    ItemId: int
    CurrencyCategoryId: int
    ApiId: str
    BaseItemTypeId: str
    Text: str
    CategoryApiId: str
    IconUrl: str
    ItemMetadata: CurrencyItemMetadata
    PriceLogs: list[PriceLogEntry]

class ScoutCurrencyResponse(TypedDict):
    CurrentPage: int
    Pages: int
    Total: int
    Items: list[ScoutCurrencyEntry]


class ScoutItemEntry(TypedDict):
        ItemId: int
        CategoryApiId: str
        Text: str
        Name: str
        Type: str
        ApiId: int
        BaseItemTypeId: int
        CurrentPrice: int
        IconUrl: str
class ScoutItemResponse(TypedDict):
    data: list[ScoutItemEntry]