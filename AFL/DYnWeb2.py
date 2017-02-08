import sys

# third-party imports
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWebKitWidgets import QWebPage
from PyQt5.QtWidgets import QApplication
import pandas as pd


class Render(QWebPage):
    """Render HTML with PyQt5 WebKit."""

    def __init__(self, html):
        self.html = None
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.mainFrame().setHtml(html)
        self.app.exec_()

    def _loadFinished(self, result):
        self.html = self.mainFrame().toHtml()
        self.app.quit()


url = 'http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T10'

# get the raw HTML
source_html = requests.get(url).text
#print(source_html)
# return the JavaScript rendered HTML
#with Display(visible=0, size=(800, 600)):
rendered_html = Render(source_html).html

# get the BeautifulSoup
soup = BeautifulSoup(rendered_html, 'html.parser')

#print(soup.prettify())
#print('title is %r' % soup.select_one('title').text)

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
    
