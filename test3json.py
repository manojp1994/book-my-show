from bs4 import BeautifulSoup		
import pandas as pd
import re
import requests

# url = r"C:\\Users\\MANOJ KUMAR\\Desktop\\python\\scrapingdemo.html" 	#  for scraping html pages on local storage
#page = open(url)
# soup = BeautifulSoup(page.read(),"html.parser")

url = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Wlc_b6iWY2w.html")   #  for scraping html pages from url 
soup = BeautifulSoup(url.content,"html.parser")
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
result=forecast_items[0]
type_of_day = result.find(class_="period-name").get_text()
desc = soup.find(class_="short-desc").get_text()
temp = soup.find(class_="temp temp-low").get_text()
img = result.find("img")
desc = img['title']
period_tags = seven_day.select(".tombstone-container .period-name")
periods = []
for pt in period_tags:
	periods.append(pt.get_text())
	#print(periods)
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img[")]

weather = pd.DataFrame({
        "period": periods, 
        "short_desc": short_descs, 
        "temp": temps, 
        "desc":descs
    })
print(weather)]