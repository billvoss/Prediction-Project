import pandas as pd
#from decimal import Decimal
teamDF = pd.read_csv('BBLTeams.csv')
batDF = pd.read_csv('BattingData.csv')
#print(batDF)
bowlDF = pd.read_csv('BowlingData.csv')

bowlDF.set_index('Name', inplace = 'true')
batDF.set_index('Name', inplace = 'true')
teamDF = teamDF.values

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
playersNotPlaying1 = []
ppName = '_'
ppTF = input('For Home Team are there any players that are not playing?')
while ppTF == 'y' or ppTF == 'yes' or ppTF == 'YES' :
    ppName = input('Player full name : ')
    playersNotPlaying1.append(ppName)
    ppTF = input('Any more players not playing? ')
    

    
    

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
playersNotPlaying2 = []
ppName = '_'
ppTF = input('For Away Team are there any players that are not playing?')
while ppTF == 'y' or ppTF == 'yes' or ppTF == 'YES' :
    ppName = input('Player full name : ')
    playersNotPlaying2.append(ppName)
    ppTF = input('Any more players not playing? ')
count2 = 0
bowlCount1 = 0
batCount1 = 0
bowlCount2 = 0
batCount2 = 0
#home team calc
while count2 <19:
    #print (row)
    #print(Team1)
    #print(teamDF.loc[:Team1])
    row1 = teamDF[count2,Team1]
    #row1 = row[Team1]#.strip('.')
    
    #print(row1)
    if count2 == 0:
        row2 = row1.rstrip(' (Captain)')
    else :
        row2 = row1
    print(row2)
    #print(row2 in bowlDF.index)
    if row2 not in playersNotPlaying1:
        if row2 in bowlDF.index :
            #BowlStat1 = float(BowlStat1) + float(bowlDF.loc[row2,'Ave'])*float(bowlDF.loc[row2,'Econ'])
            #insert bowl annalysis
            #print(type(bowlDF.loc[row2,'Ave']))
            bowlCount1 += 1
            if isinstance(bowlDF.loc[row2,'Ave'],str):
                try :
                    BowlStat1 += float(bowlDF.loc[row2,'Ave'])*float(bowlDF.loc[row2,'Econ'])
                except:
                    bowlCount1 = bowlCount1
                #print(float(bowlDF.loc[row2,'Ave'])*float(bowlDF.loc[row2,'Econ']))
            else :
                #print(float(bowlDF.loc[row2,'Ave'].values[0])*float(bowlDF.loc[row2,'Econ'].values[0]))
                BowlStat1 += float(bowlDF.loc[row2,'Ave'].values[0])*float(bowlDF.loc[row2,'Econ'].values[0])
            #AdeSix.loc[row1] = bowlDF.loc[row2]
            print('Bowl Stats :')
            print(BowlStat1)
        if row2 in batDF.index:
        #    #insert bat annalysis
            #print('true')
            #print(type(batDF.loc[row2,'Ave'])) 
            batCount1 += 1
            BatStat1 += batDF.loc[row2,'Ave']*batDF.loc[row2,'SR']
            print('Bat Stats: ')
            print(BatStat1)
            #print(BatStat1)
        #    if isinstance(batDF.loc[row2,'Ave'],str):
        #        
        #        print(float(batDF.loc[row2,'Ave'])*float(batDF.loc[row2,'SR']))
        #        BatStat1 += float(batDF.loc[row2,'Ave'])*float(batDF.loc[row2,'SR'])
        #    else :
        #        print(float(batDF.loc[row2,'Ave'].values[0])*float(batDF.loc[row2,'SR'].values[0]))
        #        BatStat1 += float(batDF.loc[row2,'Ave'].values[0])*float(batDF.loc[row2,'SR'].values[0])
            #BatStat1 += batDF.loc[row2,'Ave']*batDF.loc[row2,'SR']
    count2 +=1
    
    
count2 = 0  
#away team calc  
while count2 <19:
    row1 = teamDF[count2,Team2]
    if count2 == 0:
        row2 = row1.rstrip(' (Captain)')
    else :
        row2 = row1
    print(row2)
    if row2 not in playersNotPlaying2:
        if row2 in bowlDF.index :
            bowlCount2 += 1
            if isinstance(bowlDF.loc[row2,'Ave'],str):
                try :
                    BowlStat2 += float(bowlDF.loc[row2,'Ave'])*float(bowlDF.loc[row2,'Econ'])
                except:
                    bowlCount2 = bowlCount2
            else :
                BowlStat2 += float(bowlDF.loc[row2,'Ave'].values[0])*float(bowlDF.loc[row2,'Econ'].values[0])
            print('Bowl Stats :')
            print(BowlStat2)
        if row2 in batDF.index:
            batCount2 += 1
            BatStat2 += batDF.loc[row2,'Ave']*batDF.loc[row2,'SR']
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
print(BowlStat2 * BatStat1)
print(BowlStat1 * BatStat2)
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
print(playersNotPlaying1)
print('Team Two')
print(playersNotPlaying2)