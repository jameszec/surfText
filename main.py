from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://surfcaptain.com/forecast/virginia-beach'

# opening connection
uClient = uReq(my_url)
#loads file into variable
page_html = uClient.read()
#close page
uClient.close()

page_soup = soup(page_html, "html.parser")
forecast = page_soup.h1