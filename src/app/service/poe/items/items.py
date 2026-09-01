

from app.repository.items import read_items


def handle_item_overview():
   try:
    items = read_items()
    print(items)
    return items
   except:
     print("Error")
     return "Unable to get items"