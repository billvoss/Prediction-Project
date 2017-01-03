import pandas as pd
def TweetParser(Tweet , Team):
    teamDF = pd.read_excel('BBLTeams.xlsx')
    my_string = Tweet.split(', ')
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