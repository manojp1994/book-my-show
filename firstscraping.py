from bs4 import BeautifulSoup		
import pandas as pd
import re
import requests

url = requests.get("https://www.yelp.com/search?cflt=massage&find_loc=San+Francisco%2C+CA.html")   #  for scraping html pages from url 
soup = BeautifulSoup(url.content,"html.parser")
all_massage_places_in_sanfrancisco = soup.find(id="yelp_main_body")
time_massage_place_in_sanfrancisco = soup.find_all(class_="mtb-response-time-fast-responder")
first=time_massage_place_in_sanfrancisco[0]
spalist=[]
extracted_top_10=soup.find_all(class_="biz-name js-analytics-click")
for e in extracted_top_10[:10]:
	spalist.append(e.get_text())
print(spalist)