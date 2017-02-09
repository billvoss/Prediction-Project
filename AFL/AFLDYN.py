from bs4 import BeautifulSoup
import pandas as pd
htmlNames = ['Adelaide1','Adelaide2','Brisbane1','Brisbane2','Carlton1','Carlton2','Collingwood1','Collingwood2','Essendon1','Essendon2','Fremantle1','Fremantle2','Geelong1','Geelong2','GoldCoast1','GoldCoast2','GWS1','GWS2','Hawthorn1','Hawthorn2','Melbourne1','Melbourne2','NorthMelbourne1','NorthMelbourne2','PortAdelaide1','PortAdelaide2','Richmond1','Richmond2','StKilda1','StKilda2','SydneySwans1','SydneySwans2','WestCoast1','WestCoast2','WesternBulldogs1','WesternBulldogs2']
def htmlToCSV(name):
    HTML1 = name +'.html'
    HTML2 = name.rstrip('1') + '2.html'
    CSV = name.rstrip('1') + '.csv'
    print(HTML1)
    result = open(HTML1)
    c = result
    soup = BeautifulSoup(c,"html.parser")
    sTable = soup.find_all('table', class_='ladder zebra player-ratings')
    B=[]
    C=[]
    D=[]
    E=[]
    F=[]
    for row in sTable:
        cells = row.findAll('td')
        i=0
        while(i<len(cells)):
            B.append(cells[i+1].find('span').get_text().strip())
            C.append(cells[i+2].find('span').get_text().strip())
            D.append(cells[i+3].find('span').get_text().strip())
            E.append(cells[i+4].get_text().strip())
            F.append(cells[i+5].get_text().strip())
            i+=6
    result = open(HTML2)
    c = result
    soup = BeautifulSoup(c,"html.parser")
    sTable = soup.find_all('table', class_='ladder zebra player-ratings')       
    for row in sTable:
        cells = row.findAll('td')
        i=0
        while(i<len(cells)):
            B.append(cells[i+1].find('span').get_text().strip())
            C.append(cells[i+2].find('span').get_text().strip())
            D.append(cells[i+3].find('span').get_text().strip())
            E.append(cells[i+4].get_text().strip())
            F.append(cells[i+5].get_text().strip())
            i+=6
    df=pd.DataFrame(B,columns=['Name'])
    df['Club']=C
    df['Position']=D
    df['Trend']=E
    df['Points']=F
    df.set_index('Name', inplace = 'true')
    df.to_csv(CSV)
    
    print(df)

j = 0
while j<36:
    htmlToCSV(htmlNames[j])  
    j += 2 
        
