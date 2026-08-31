# url reference: https://api.poe2scout.com/poe2/Leagues/runes/Currencies/ByCategory?Category=currency&ReferenceCurrency=exalted&Page=2&PerPage=25&DataPoints=8&FrequencyHours=6
import requests
import aiohttp
URL = "https://api.poe2scout.com/poe2/Leagues/runes/Currencies/ByCategory?Category=currency&ReferenceCurrency=exalted&Page=1&PerPage=50&DataPoints=8&FrequencyHours=24"
BASE_URL : str = "https://api.poe2scout.com"
URL_PATH : str = "/poe2/Leagues/runes/Currencies/ByCategory"


async def getPoeScoutOverview():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(URL) as response:
                data = await response.json()
                print(data)
    except requests.exceptions.HTTPError as error:
        print(error)

    