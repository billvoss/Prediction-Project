'''
Created on 9Dec.,2016

@author: Adam Kitto
'''
import requests
result = requests.get("http://bigbashboard.com/statistics/bbl/player/bowling/economy-rate")
#r = requests.get('http://github.com', allow_redirects=False)

c = result.content
from bs4 import BeautifulSoup
import pandas as pd
#think it could be working now :)
soup = BeautifulSoup(c,"html.parser")



#print (soup.prettify())
#kinda working

sTable = soup.find_all('table', class_='statistic-table')

result2 = requests.get("http://bigbashboard.com/statistics/bbl/player/bowling/average/2")
c2 = result2.content   
soup2 = BeautifulSoup(c2,"html.parser")
sTable2 = soup2.find_all('table', class_='statistic-table') 
#print(soup.find_all('table', class_='ladder zebra player-ratings'))
A=[]
B=[]
C=[]
D=[]
E=[]
for row in sTable:#.findAll("tr"):
    cells = row.findAll('td')
    #print (cells[1].find_all('span'))
    #span.r-hide-for-small
    #if len(cells)==6: #Only extract table body not heading
    i=0
    while(i<2000):
        
        #A.append(cells[i].get_text().strip())
        #print(cells[i].get_text().strip())
        A.append(cells[i+1].get_text().strip())
        B.append(cells[i+3].get_text().strip())
        C.append(cells[i+8].get_text().strip())
        D.append(cells[i+9].get_text().strip())
        E.append(cells[i+10].get_text().strip())
        i+=20
for row in sTable2:#.findAll("tr"):
    cells = row.findAll('td')
    #print (cells[1].find_all('span'))
    #span.r-hide-for-small
    #if len(cells)==6: #Only extract table body not heading
    i=0
    while(i<1400):
        
        #A.append(cells[i].get_text().strip())
        #print(cells[i].get_text().strip())
        A.append(cells[i+1].get_text().strip())
        B.append(cells[i+3].get_text().strip())
        C.append(cells[i+8].get_text().strip())
        D.append(cells[i+9].get_text().strip())
        E.append(cells[i+10].get_text().strip())
        i+=20

        
#print(cells[2].find('span').get_text().strip())
#print(A[0])
#import pandas to convert list to data frame
df=pd.DataFrame(A,columns=['Name'])
df['Matches']=B
df['Ave']=C
df['Econ']=D
df['SR']=E
df.set_index('Name', inplace = 'true')
#print(df)
df.to_csv( 'BowlingData.csv', encoding='utf-8')
print('Scraping Completed \n')
print('CSV updated')  
