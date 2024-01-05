import re
import requests
from bs4 import BeautifulSoup

site = 'https://2023.holidayhackchallenge.com/sea/fishdensityref.html'

imagesite = 'https://2023.holidayhackchallenge.com/sea/'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]


for url in urls:
    filename = re.search(r'/([ .,\w_-]+[.](png))$', url)
    if not filename:
         print("Regex didn't match with the url: {}".format(url))
         continue
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            # sometimes an image source can be relative 
            # if it is provide the base url which also happens 
            # to be the site variable atm. 
            url = '{}{}'.format(imagesite, url)
        response = requests.get(url)
        f.write(response.content)