'''
Created on 9Dec.,2016

@author: Adam Kitto
'''
import requests
result = requests.get("http://www.afl.com.au/stats/player-ratings/overall-standings#page/2" , timeout = 10)
#r = requests.get('http://github.com', allow_redirects=False)

c = result.content
from bs4 import BeautifulSoup
import pandas as pd
#think it could be working now :)
soup = BeautifulSoup(c,"html.parser")

#print (soup.prettify())
#kinda working

sTable = soup.find_all('table', class_='ladder zebra player-ratings')
#print(soup.find_all('table', class_='ladder zebra player-ratings'))
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
for row in sTable:#.findAll("tr"):
    cells = row.findAll('td')
    #print (cells[1].find_all('span'))
    print("Hello")
    #span.r-hide-for-small
    #if len(cells)==6: #Only extract table body not heading
    i=0
    while(i<240):

        A.append(cells[i].get_text().strip())
        #print(cells[1].find('span').get_text().strip())
        B.append(cells[i+1].find('span').get_text().strip())
        C.append(cells[i+2].find('span').get_text().strip())
        D.append(cells[i+3].find('span').get_text().strip())
        E.append(cells[i+4].get_text().strip())
        F.append(cells[i+5].get_text().strip())
        i+=6


#print(cells[2].find('span').get_text().strip())
#print(A[0])
#import pandas to convert list to data frame
df=pd.DataFrame(A,columns=['Number'])
df['Name']=B
df['Club']=C
df['Position']=D
df['Trend']=E
df['Points']=F
print(df)
