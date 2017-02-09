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



for row in sTable:
    cells = row.findAll('ul')
#    print (cells[0].get_text())
#    print("Hello")
#    print(cells[0])
    players1 = cells[0].find_all('li')
    #print(cells[2])
##    print ("hello")
#    print(players1)
#    print(len(players1))
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
    A.append(players1)
    B.append(players2)
H1=A[0]

A1=B[0]

H2=A[1]

A2=B[1]

H3=A[2]

A3=B[2]

H4=A[3]

A4=B[3]

H5=A[4]

A5=B[4]

H6=A[5]

A6=B[5]

H7=A[6]

A7=B[6]

H8=A[7]

A8=B[7]

H9=A[8]

A9=B[8]  
#print(A)

'''
    for i in players1[2]:
        
        del i[0:4]
        print(i)
'''
    


#import pandas to convert list to data frame
df = pd.DataFrame(H1,columns=['G1 Home Team'])
df['G1 Away Team']=A1
df['G2 Home Team']=H2
df['G2 Away Team']=A2
df['G3 Home Team']=H3
df['G3 Away Team']=A3
df['G4 Home Team']=H4
df['G4 Away Team']=A4
df['G5 Home Team']=H5
df['G5 Away Team']=A5
df['G6 Home Team']=H6
df['G6 Away Team']=A6
df['G7 Home Team']=H7
df['G7 Away Team']=A7
df['G8 Home Team']=H8
df['G8 Away Team']=A8
df['G9 Home Team']=H9
df['G9 Away Team']=A9
##df['Club']=C
#df['Position']=D
#df['Trend']=E
#df['Points']=F
print(df)
df.to_csv("TeamLists.csv")
