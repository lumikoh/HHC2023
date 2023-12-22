import json

playerData = open('playerData.json')

data = json.load(playerData)

caughtFishies = []

for i in data["fishCaught"]:
    caughtFishies.append("./images/"+i["name"]+".png")