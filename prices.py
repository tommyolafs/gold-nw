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

items = []
for item in itemsUncleaned:
    statsRaw = item.split(", ")
    stats = {}
    for stat in statsRaw:
        statSplit = stat.split(": ")

        print(statSplit) # ItemName = "Captain Quicksilver\\\'s Lamp, Bronze Replica"
        statName = statSplit[0].strip('"')
        statValue = statSplit[1].strip('"')
        
        try:
            statValue = float(statValue)
        except ValueError:
            pass

        stats[statName] = statValue
    
    items.append(stats)

print(items)