from bs4 import BeautifulSoup
import requests as rq

url = "https://nwmarketprices.com/api/latest-prices/58/"

itemsRaw = (
    "Weapon Matrix", "Jewelry Matrix", "Armor Matrix",
    "Tempered Cast", "Enchanted Handle",
    "Prismatic Ingot", "Prismatic Leather", "Prismatic Cloth", "Prismatic Planks", "Prismatic Block"
)

#for item in items:
site = rq.get(url)
html = str(site.content)

itemsRaw = html.split("}")[0:-1]



itemsRaw[0] = itemsRaw[0][3:]
print(itemsRaw[0])
print(itemsRaw[-1], "\n")

itemsUncleaned = []

for index, item in enumerate(itemsRaw):
    if index == 0:
        item = item[1:]
    else:
        item = item[3:]
    
    itemsUncleaned.append(item)

print(itemsUncleaned[0])
print(itemsUncleaned[4])
print(itemsUncleaned[-1])

for item in itemsUncleaned:
    pass