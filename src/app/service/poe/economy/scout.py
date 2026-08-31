# url reference: https://api.poe2scout.com/poe2/Leagues/runes/Currencies/ByCategory?Category=currency&ReferenceCurrency=exalted&Page=2&PerPage=25&DataPoints=8&FrequencyHours=6
import asyncio

import requests
import aiohttp

from app.model.poe import ScoutCurrencyResponse, Item
from app.repository.items import insert_item
URL = "https://api.poe2scout.com/poe2/Leagues/runes/Currencies/ByCategory?Category=currency&ReferenceCurrency=exalted&Page=1&PerPage=50&DataPoints=8&FrequencyHours=24"
BASE_URL : str = "https://api.poe2scout.com"
URL_PATH : str = "/poe2/Leagues/runes/Currencies/ByCategory"


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

def formatItemData(data: ScoutCurrencyResponse) -> list[Item]:
    formattedItemData: list[Item] = []
    for item in data.get("Items"):
        formattedItem:Item = {
            "category": item["CategoryApiId"],
            "description": item["ItemMetadata"]["description"],
            "name":item["ItemMetadata"]["name"],
            "item_id":item["ItemId"],
            "icon_url": item["ItemMetadata"]["icon"]
        }
        formattedItemData.append(formattedItem)
    return formattedItemData
    

def handleItemData():
    data = asyncio.run(getPoeScoutOverview())
    if data is None:
        return
    formattedItemData = formatItemData(data)
    for item in formattedItemData:
        insert_item(item)


    # item: Item = {"name":"Mirror of Kalandra","item_id":295,"description":"Right click this item then left click an equipable non-unique item to apply it. Mirrored copies cannot be modified.","category":"currency","icon_url":"https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvQ3VycmVuY3lEdXBsaWNhdGUiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MSwicmVhbG0iOiJwb2UyIn1d/b7f5cc7884/CurrencyDuplicate.png"}
    # insert_item(item)