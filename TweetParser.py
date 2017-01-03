import pandas as pd
def TweetParser(Tweet , Team):
    teamDF = pd.read_excel('BBLTeams.xlsx')
    my_string = Tweet.split(', ')
    
    count3 = 0
    while count3 <11:
        if ' (c)' in my_string[count3]:
            my_string[count3] = my_string[count3].rstrip(' (c)')
        if ' ' in my_string[count3]:
            my_string[count3] = my_string[count3].split(' ')
            print(my_string[count3][0])
            ###something wrong here
            del my_string[count3][0]
            my_string[count3] = ''.join(my_string[count3])
            print(my_string[count3])
        count3 += 1
        print(my_string[count3])
    new_string = []
    count = 0
    count2 = 0
    while count < 11:
        count2 = 0
        
        
        while count2 < 22:
            #print(teamDF.loc[count2,'Sydney Sixers'])
            try :
                if my_string[count] in teamDF.iloc[count2,Team]:
                    new_string.append(teamDF.iloc[count2 , Team])
            except :
                count2 = count2
            count2 += 1
        count += 1
    return new_string