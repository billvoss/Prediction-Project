import requests
result = requests.get("http://afltables.com/afl/teams/allteams/last20.html" , timeout = 10)
#r = requests.get('http://github.com', allow_redirects=False)

c = result.content
from bs4 import BeautifulSoup
import pandas as pd
#think it could be working now :)
soup = BeautifulSoup(c,"html.parser")

#print (soup.prettify())
#kinda working

sTable = soup.find_all('table', class_='sortable')
#print(soup.find_all('table', class_='ladder zebra player-ratings'))
A=[]
B=[]
C=[]
D=[]

for row in sTable[0]:#.findAll("tr"):
    cells = row.findAll('td')
    #print (cells[1].find_all('span'))

    #span.r-hide-for-small
    #if len(cells)==6: #Only extract table body not heading
    i=0
    #print(len(cells))
    #print(cells)
    while(i<len(cells)):
        count = 0
        if(cells[i].get_text().strip() != "Brisbane Bears" and cells[i].get_text().strip() != "University" and cells[i].get_text().strip() != "Fitzroy"):
            A.append(cells[i].get_text().strip())
            #print(cells[i].get_text().strip())
            if (cells[i+1].get_text().strip() == ''):
                B.append(0)
            else:
                B.append(cells[i+1].get_text().strip())
#            print(cells[i+1].get_text().strip())
            C.append(cells[i+7].get_text().strip())
#           print(cells[i+7].get_text().strip())
            k = 0
            winloss = cells[i+7].get_text().strip()
            while (k<len(winloss)):
                if (winloss[k] == 'W'):
                    count += k+1
                elif(winloss[k] == 'L'):
                    count -= (k+1)
                k += 1
            D.append(count)        
        i+=8


#print(cells[2].find('span').get_text().strip())
#print(A[0])
#import pandas to convert list to data frame
df=pd.DataFrame(A,columns=['Club'])
df['Wins']=B
df['Visual']=C
df['Weighted Form']=D
df.set_index('Club', inplace = 'true')
df.to_csv('RecentForm.csv')
print(df)
