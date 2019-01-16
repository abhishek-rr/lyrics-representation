import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv

pd.set_option('display.expand_frame_repr', False)

try:
	website = pd.read_html('https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_2018')	
	search_list = website[0][1].tolist()

except Exception as e:
	print(e)

url1="https://www.google.com/search?hl=en&source=hp&ei=ECkuXNGRDcSBvQSvsL2ACg&q="
url2="+metrolyrics&btnK=Google+Search&oq=perfec&gs_l=psy-ab.3.0.0l2j0i131l2j0l6.10775.12224..13807...3.0..0.205.928.0j6j1......0....1..gws-wiz.....6..35i39.CGteOpZ-Prc"

#links_for_songs = []

csv_file = open('lyrics_site_list.csv','w')
csv_writer=csv.writer(csv_file)

for song in search_list:
	song = song[1:-1]
	new_song = song.split(" ")
	final = ""
	for word in new_song:
		final = final + "+" + word 
	final = final[1:]
	g_search = url1 + final + url2
	
	source = requests.get(g_search).text
	soup = BeautifulSoup(source,'lxml')
	lyrics_link = soup.find('div',class_="hJND5c")
	csv_writer.writerow([lyrics_link.cite.text])
	#links_for_songs.append(lyrics_link.cite.text)

# print(links_for_songs)


