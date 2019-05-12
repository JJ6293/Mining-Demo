#Created by Justin James

#Importing tools
import bs4
import urllib
import urllib.request
from bs4 import BeautifulSoup 
import csv

url = 'https://www.imdb.com/title/tt0944947/episodes?ref_=tt_ov_epl'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page,"html.parser")

episode_title = soup.find('div',{"class":"list detail eplist"}).find('strong').text
episode_rating = soup.find('div',{"class":"ipl-rating-widget"}).find('span',{"class":"ipl-rating-star__rating"}).text

print(soup.title.text)

print(episode_title)
print(episode_rating)