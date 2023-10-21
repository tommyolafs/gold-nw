from bs4 import BeautifulSoup
import requests as rq

url = 'https://nwmarketprices.com/api/latest-prices/58/'

lookupItems = (
    'Weapon Matrix', 'Jewelry Matrix', 'Armor Matrix',
    'Tempered Cast', 'Enchanted Handle',
    'Prismatic Ingot', 'Prismatic Leather', 'Prismatic Cloth', 'Prismatic Planks', 'Prismatic Block'
)

site = rq.get(url)
html = str(site.content)

itemsRaw = html.split('}')[0:-1]

itemsUncleaned = []

for index, item in enumerate(itemsRaw):
    if index == 0:
        item = item[4:]
    else:
        item = item[3:]
    
    itemsUncleaned.append(item)

items = []
for item in itemsUncleaned:
    statsRaw = item.split(', "')
    stats = {}
    for stat in statsRaw:
        statSplit = stat.split(': ')

        statName = statSplit[0].strip('"')
        statValue = statSplit[1].strip('"')
        
        try:
            statValue = float(statValue)
        except ValueError:
            pass

        stats[statName] = statValue
    
    items.append(stats)

pricesPath = './prices.txt'

with open(pricesPath, 'w') as file:
    for item in items:
        name = item['ItemName']
        price = item['Price']
        quantity = item['Qty']

        itemInfo = f"{name} | {price} | {quantity}"
        file.write(itemInfo + "\n")