import urllib
#python library for pulling data
from bs4 import BeautifulSoup
import csv
from datetime import datetime

handle = input("Whose tweets would you like to see? ")
url = "https://twitter.com/"+handle
page = urllib.urlopen(url)
soup = BeautifulSoup(page, "html.parser")

f=soup.title.text    
m=soup.find('div',{"class":"ProfileHeaderCard"}).find('p').text

i=1
k=[]
#append the tweets in lisk name k
for tweet in soup.findAll('div',{"class":'content'}):
	k.append(tweet.find('p').text)

#writing the tweets
#tweets save in file
with open('/home/lakshay/Music/filename.csv','a') as csv_file:
	writer=csv.writer(csv_file)
	writer.writerow([f,k,m,datetime.now()])
