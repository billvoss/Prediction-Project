import pandas as pd
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
playersPlaying1 = []
ppName = '_'
print('Please input home team Names')
playerCount = 0
while playerCount < 11 :
    ppName = input('Player full name : ')
    playersPlaying1.append(ppName)
    playerCount += 1
    

    
    

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
playersPlaying2 = []
ppName = '_'
print('Please input away team Names')
playerCount = 0
while playerCount < 11 :
    ppName = input('Player full name : ')
    playersPlaying2.append(ppName)
    playerCount += 1
    
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
            except:
                bowlCount1 = bowlCount1
        else :
            BowlStat1 += float(bowlDF.loc[row1,'Ave'].values[0])*float(bowlDF.loc[row1,'Econ'].values[0])
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
                BowlStat2 += float(bowlDF.loc[row1,'Ave'])*float(bowlDF.loc[row1,'Econ'])
            except:
                bowlCount2 = bowlCount2
        else :
            BowlStat2 += float(bowlDF.loc[row1,'Ave'].values[0])*float(bowlDF.loc[row1,'Econ'].values[0])
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
if Home[Team1] < Away[Team2]:
    adjust = (Away[Team2] - Home[Team1])/100 + 1
    result = (BowlStat2 * BatStat1)/(adjust) - (BowlStat1 * BatStat2*adjust)
else :
    adjust = (Home[Team1] - Away[Team2])/100 + 1
    result = (BowlStat2 * BatStat1*adjust) - (BowlStat1 * BatStat2)/adjust
###enter in adjust part
print('result is:  ')
print(result)
print(playersPlaying1)
print('Team Two')
print(playersPlaying2)