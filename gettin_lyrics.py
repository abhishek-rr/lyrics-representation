import csv
from bs4 import BeautifulSoup
import requests
import pickle
import re
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from matplotlib import style
style.use('fivethirtyeight')

def con_to_pickle():
	try:
		csv_file = open('lyrics_site_list.csv','r')
		csv_reader = csv.reader(csv_file)

		save_var = ""

		for row in csv_reader:
			final_site = 'http://' + row[0]
			source = requests.get(final_site).text
			soup = BeautifulSoup(source,'lxml')
			lyrics = soup.findAll('p',class_='verse')
			for lyric in lyrics:
				save_var = save_var + lyric.text
		print(save_var)
		pickle_out = open('ly.pickle','wb')
		pickle.dump(save_var,pickle_out)
		pickle_out.close()	

	except Exception as e:
		raise e

		
#con_to_pickle()

pickle_in = open("ly.pickle",'rb')
sum_lyrics = pickle.load(pickle_in)

word_data = {}
for word in re.findall(r"[\w']+", sum_lyrics):
	word_list = [word]
	word_tagged = nltk.pos_tag(word_list)

	if word_tagged[0][1] in ('NN','NNS','JJR','JJS','NNP','NNPS','VB'):
		if word.lower() in word_data:
			word_data[word.lower()] += 1
		else:
			word_data[word.lower()] = 1

#df = pd.DataFrame([word_data])
#df = pd.DataFrame(word_data, index=[0])
#print(df)
sorted_dict = sorted(word_data.items(), key = lambda x:x[1], reverse = True)
d1=[]
d2=[]

for i in range(0,20):
	d1.append(sorted_dict[i][0])
	d2.append(sorted_dict[i][1])



plt.bar(d1,d2,label = "lyrics")
plt.xlabel('words')
plt.ylabel('number of times it has occoured')
plt.title('Words used in pop songs 2018')
plt.show()