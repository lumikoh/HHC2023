import glob
from PIL import Image
import numpy as np
import json

playerData = open('playerData.json')

data = json.load(playerData)

caughtFishies = []

for i in data["fishCaught"]:
    caughtFishies.append("./images/"+i["name"]+".png")

images = []
for f in glob.iglob("./images/*"):
    if(f in caughtFishies):
        continue
    images.append(Image.open(f).convert("L"))

image1 = images[0]

print(len(images))

for i in range(1,len(images)):
    image1 = Image.blend(image1, images[i], (1/(i+1)))

image1.save("result.png")