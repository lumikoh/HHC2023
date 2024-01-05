# Fishing Guide
I did not include my own playerData here, but if you want to try this out,
you can go to the Ahoy! developer console and type "playerData, copy the object
and save it as playerData.json. The script I made uses only the caught fish 
part to remove any fish that has already been caught.

What I did here was that I found the data for the different fishes 
[here](https://2023.holidayhackchallenge.com/sea/fishdensityref.html).
The link was hidden in the source code of the fishing minigame.
The closer to white the area is, the higher chance to catch it there. 
I did not really analyze it further, and decided to take an approach where 
I overlayed each image with each other, giving me the best areas to catch
whatever fishes I'm missing. The script for forming the image is in the file
overlayimages.py. It did become quite evident that there was a certain spot
where one of the fishes needed to be caught...

![example of the overlayed images](../images/fish_example.png)

I also made a TamperMonkey script to automate the fishing process, which is
found in fishing_script.js. I tried to make it as elegant as possible, so that
it would not try to fish unless it was permitted (it keeps track of the status
of the HTML element). Still, it's recommended to only keep it on when staying
AFK to catch the fish.

I let the script run overnight in a suitable spot, in the morning I had 
finished the fishing log.