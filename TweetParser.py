import pandas as pd
def TweetParser(Tweet , Team):
    teamDF = pd.read_excel('BBLTeams.xlsx')
    my_string = Tweet.split(', ')
    
    count3 = 0
    while count3 <11:
        if ' (c)' in my_string[count3]:
            my_string[count3] = my_string[count3].rstrip(' (c)')
        if ' (wk)' in my_string[count3]:
            my_string[count3] = my_string[count3].rstrip(' (wk)')
        #if ' ' in my_string[count3]:
        #    my_string[count3] = my_string[count3].split(' ')
            #print(my_string[count3][0])
            ###something wrong here
        #    del my_string[count3][0]
        #    my_string[count3] = ''.join(my_string[count3])
        
        count3 += 1
        
    new_string = []
    count = 0
    count2 = 0
    while count < 11:
        count2 = 0
        
        try :
            while count2 < 22:
                #print(teamDF.loc[count2,'Sydney Sixers'])
                
                    if my_string[count] in teamDF.iloc[count2,Team]:
                        new_string.append(teamDF.iloc[count2 , Team])
                                   
                    ###split based on this, then search for first name and last name. You can do this on the bus easy
                    count2 += 1
        except :
                count2 = count2
                if my_string[count] == 'M.Marsh'  or my_string[count] == 'M Marsh' :
                    new_string.append('Mitch Marsh')
                elif my_string[count] == 'S.Marsh'  or my_string[count] == 'S Marsh' :
                    new_string.append('Shaun Marsh')     
        count += 1
    return new_string