# url reference: https://api.poe2scout.com/poe2/Leagues/runes/Currencies/ByCategory?Category=currency&ReferenceCurrency=exalted&Page=2&PerPage=25&DataPoints=8&FrequencyHours=6
import asyncio

import requests
import aiohttp

from app.model.poe import ScoutCurrencyResponse, Item, ScoutItemEntry, ScoutItemResponse
from app.repository.items import insert_item
from app.repository.currency import insert_price_log
URL = "https://api.poe2scout.com/poe2/Leagues/runes/Currencies/ByCategory?Category=currency&ReferenceCurrency=exalted&Page=1&PerPage=50&DataPoints=8&FrequencyHours=24"
ITEM_URL = "https://api.poe2scout.com/poe2/Leagues/runes/Items"

BASE_URL : str = "https://api.poe2scout.com"
URL_PATH : str = "/poe2/Leagues/runes/Currencies/ByCategory"
TRADE_CURRENCY = "exalted"
INTERVAL = 24


async def getPoeScoutOverview() -> ScoutCurrencyResponse | None:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(URL) as response:
                data: ScoutCurrencyResponse = await response.json()
                print(data)
                return data 
    except requests.exceptions.HTTPError as error:
        print(error)
        return None
    
async def getPoeScoutItemOverview() -> ScoutItemResponse | None:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(ITEM_URL) as response:
                data: ScoutItemResponse = await response.json()
                print(data)
                return data 
    except requests.exceptions.HTTPError as error:
        print(error)
        return None

def formatItemData(data: ScoutCurrencyResponse) -> list[Item]:
    formattedItemData: list[Item] = []
    for item in data.get("Items"):
        formattedItem:Item = {
            "category": item["CategoryApiId"],
            "description": item["ItemMetadata"]["description"],
            "name":item["ItemMetadata"]["name"],
            "item_id":item["ItemId"],
            "icon_url": item["ItemMetadata"]["icon"],
            "price_data":item["PriceLogs"]
        }
        formattedItemData.append(formattedItem)
    return formattedItemData
    
def formatItemResponse(data: list[ScoutItemEntry]) -> list[Item]:
    formattedItemData: list[Item] = []
    for item in data:
        formattedItem: Item = {
            "category": item["CategoryApiId"],
            "description": item["Text"],
            "name":item["Name"],
            "item_id":item["ItemId"],
            "icon_url": item["IconUrl"]
        }
        formattedItemData.append(formattedItem)
    return formattedItemData

def handleItemOverview() -> None:
    data = asyncio.run(getPoeScoutItemOverview())
    if data is None:
        return
    formattedItemData = formatItemResponse(data)
    for item in formattedItemData:
        insert_item(item)

def handleItemData():
    data = asyncio.run(getPoeScoutOverview())
    if data is None:
        return
    formattedItemData = formatItemData(data)
    for item in formattedItemData:
        insert_item(item)
        price_data = item.get("price_data")
        if price_data is None:
            continue
        for price in price_data:
            if price is None:
                continue
            print(price)
            insert_price_log(item["item_id"], TRADE_CURRENCY,INTERVAL, price)
