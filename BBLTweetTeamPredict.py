import pandas as pd
import TweetParser
#from decimal import Decimal
batDF = pd.read_csv('BattingData.csv')
#print(batDF)
bowlDF = pd.read_csv('BowlingData.csv')

bowlDF.set_index('Name', inplace = 'true')
batDF.set_index('Name', inplace = 'true')

#Teams
#Adelaide Strikers
#Brisbane Heat
#Hobart Hurricanes
#Melbourne Renegades
#Melbourne Stars
#Perth Scorchers
#Sydney Sixers
#Sydney Thunder

#Team1 = -1
#Team2 = -1
BowlStat1 = 0
BatStat1 = 0
BowlStat2 = 0
BatStat2 = 0
BowlStat11 = 0
BowlStat21 = 0
Team1 = -1
Team2 = -1

while Team1 == -1:
    Team1 = input('Input home team: ')
    if Team1 == 'A':
        Team1 = 0
    elif Team1 == 'B':
        Team1 = 1
    elif Team1 == 'H':
        Team1 = 2
    elif Team1 == 'MR':
        Team1 = 3
    elif Team1 == 'MS':
        Team1 = 4
    elif Team1 == 'P':
        Team1 = 5
    elif Team1 == 'SS':
        Team1 = 6
    elif Team1 == 'ST':
        Team1 = 7
    else :
        print('Invalid Team')
        Team1=-1
TTP = input('Input tweet containing team list for home team : ')

playersPlaying1 = TweetParser.TweetParser(TTP,Team1)
while Team2 == -1:
    Team2 = input('Away Team: ')
    if Team2 == 'A':
        Team2 = 0
        
    elif Team2 == 'B':
        Team2 = 1
    elif Team2 == 'H':
        Team2 = 2
    elif Team2 == 'MR':
        Team2 = 3
    elif Team2 == 'MS':
        Team2 = 4
    elif Team2 == 'P':
        Team2 = 5
    elif Team2 == 'SS':
        Team2 = 6
    elif Team2 == 'ST':
        Team2 = 7
    else :
        print('Invalid Team')
        Team2=-1
TTP2 = input('Input tweet containing team list for away team : ')
playersPlaying2 = TweetParser.TweetParser(TTP2 , Team2)
print(playersPlaying1)
print(playersPlaying2)    
count2 = 0
bowlCount1 = 0
batCount1 = 0
bowlCount2 = 0
batCount2 = 0
#home team calc
while count2 <11:
    row1 = playersPlaying1[count2]
    row1 = row1.strip()
    print(row1)
    if row1 in bowlDF.index :
        bowlCount1 += 1
        if isinstance(bowlDF.loc[row1,'Ave'],str):
            try :
                BowlStat1 += float(bowlDF.loc[row1,'Ave'])*float(bowlDF.loc[row1,'Econ'])
                BowlStat11 += float(bowlDF.loc[row1,'Econ'])
            except:
                bowlCount1 = bowlCount1
        else :
            BowlStat1 += float(bowlDF.loc[row1,'Ave'].values[0])*float(bowlDF.loc[row1,'Econ'].values[0])
            BowlStat11 += float(bowlDF.loc[row1,'Econ'].values[0])
            print('Bowl Stats :')
            print(BowlStat1)
    if row1 in batDF.index:
        batCount1 += 1
        BatStat1 += batDF.loc[row1,'Ave']*batDF.loc[row1,'SR']
        print('Bat Stats: ')
        print(BatStat1)
    count2 +=1
    
    
count2 = 0  
#away team calc  
while count2 <11:
    row1 = playersPlaying2[count2]
    row1 = row1.strip()
    print(row1)
    if row1 in bowlDF.index :
        bowlCount2 += 1
        if isinstance(bowlDF.loc[row1,'Ave'],str):
            try :
                BowlStat2 += float(bowlDF.loc[row1,'Econ'])*float(bowlDF.loc[row1,'Ave'])
                BowlStat21 += float(bowlDF.loc[row1,'Econ'])
            except:
                bowlCount2 = bowlCount2
        else :
            BowlStat2 += float(bowlDF.loc[row1,'Ave'].values[0])*float(bowlDF.loc[row1,'Econ'].values[0])
            BowlStat21 += float(bowlDF.loc[row1,'Econ'].values[0])
            print('Bowl Stats :')
            print(BowlStat2)
    if row1 in batDF.index:
        batCount2 += 1
        BatStat2 += batDF.loc[row1,'Ave']*batDF.loc[row1,'SR']
        print('Bat Stats: ')
        print(BatStat2)
    count2 +=1
BowlStat1 = BowlStat1/bowlCount1
BatStat1 = BatStat1/batCount1
BowlStat2 = BowlStat2/bowlCount2
BatStat2 = BatStat2/batCount2
print(BowlStat1)
print(BatStat1)
print(BowlStat2)
print(BatStat2)
#print(BowlStat2 * BatStat1)
#print(BowlStat1 * BatStat2)
Home = (45.5,38.1,50.0,66.67,40.91,62.5,46.45,18.18)
Away = (57.14,52.17,43.48,64.0,52.38,60.87,53.55,31.82)
Home2 = (Home[0]-Away[0],Home[1]-Away[1],Home[2]-Away[2],Home[3]-Away[3],Home[4]-Away[4],Home[5]-Away[5],Home[6]-Away[6],Home[7]-Away[7],)
if Home[Team1] < Away[Team2]:
    adjust = (Away[Team2] - Home[Team1])/100 + 1
    result = (BowlStat2 * BatStat1)/(adjust) - (BowlStat1 * BatStat2*adjust)
else :
    adjust = (Home[Team1] - Away[Team2])/100 + 1
    result = (BowlStat2 * BatStat1*adjust) - (BowlStat1 * BatStat2)/adjust
result2 = (BowlStat2 * BatStat1*(Home2[Team1]/100 + 1))-(BowlStat1 * BatStat2*(-Home2[Team2]/100 + 1))
result3 = BowlStat2 * BatStat1 - BowlStat1 * BatStat2
result4 = (BowlStat21 * BatStat1*(Home2[Team1]/100 + 1))-(BowlStat11 * BatStat2*(-Home2[Team2]/100 + 1))
result5 = (BatStat1*(Home2[Team1]/100 + 1))-(BatStat2*(-Home2[Team2]/100 + 1))
result6 = ((BowlStat21 *(Home2[Team1]/100 + 1))-(BowlStat11 *(-Home2[Team2]/100 + 1)))
###enter in adjust part
print('result is:  ')
print(result)
print('Other Algorithm (more accurate adjustment):  ')
print(result2)
print('No adjustment:  ')
print(result3)
print('Econ 1 : ')
print(result4)
print('Just Bat')
print(result5)
print('Just Econ: ')
print(result6)
print(playersPlaying1)
print('Team Two')
print(playersPlaying2)