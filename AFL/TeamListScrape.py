import requests
website = input('Please paste in line up webpage:  ')
result = requests.get(website , timeout = 10)
#r = requests.get('http://github.com', allow_redirects=False)

c = result.content
from bs4 import BeautifulSoup
import pandas as pd
#think it could be working now :)
soup = BeautifulSoup(c,"html.parser")

#print (soup.prettify())
#kinda working

sTable = soup.find_all('div', class_="list-inouts")
#print(sTable)#print(soup.find_all('table', class_='ladder zebra player-ratings'))

A=[]

B=[]

C=[]

D=[]

E=[]

F=[]

G=[]

H=[]

I=[]

for row in sTable:#.findAll("tr"):
#   print("test")
    cells = row.findAll('ul')
    print (cells[0].get_text())
#    print("Hello")
#    print(cells[0])
    players1 = cells[0].find_all('li')
    print(len(players1))
    i = 0
    while i < len(players1):
        if i > 0:
            players1[i] = players1[i].get_text().split(' ')
            del players1[i][0:4]
            players1[i] = ' '.join(players1[i])
#            print(players1[i])
        else:
            players1[i] = players1[i].get_text()
#            print(players1[i])
        i += 1
    players2 = cells[1].find_all('li')
    i = 0
    while i < len(players2):
        if i > 0:
            players2[i] = players2[i].get_text().split(' ')
            del players2[i][0:4]
            players2[i] = ' '.join(players2[i])
#            print(players2[i])
        else:
            players2[i] = players2[i].get_text()
#            print(players2[i])
        i += 1
        
A = players1
B = players2

'''
    for i in players1[2]:
        
        del i[0:4]
        print(i)
'''
    


#import pandas to convert list to data frame
df=pd.DataFrame(A,columns=['Home Team'])
df['Away Team']=B
##df['Club']=C
#df['Position']=D
#df['Trend']=E
#df['Points']=F
print(df)
