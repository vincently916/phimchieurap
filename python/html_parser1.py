from unidecode import unidecode
import requests
from bs4 import BeautifulSoup

url = "http://www.nytimes.com"
r = requests.get(url)

r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")

heading = soup.select("[class~=story-heading]")

for item in heading:
 
 print item.text.strip().encode('utf-8')
 
 
