import pandas as pd
teamDF = pd.read_excel('BBLTeams.xlsx')
my_string = 'Hughes, Roy, Maddinson, Henriques, Haddin, Billings, Botha, Abbott, Dwarshuis, Somerville, Thornton'
my_string = my_string.split(', ')
new_string = []
print(my_string)
count = 0
count2 = 0
print(teamDF)
while count < 11:
    count2 = 0
    while count2 < 22:
        #print(teamDF.loc[count2,'Sydney Sixers'])
        try :
            if my_string[count] in teamDF.loc[count2,'Sydney Sixers']:
                new_string.append(teamDF.loc[count2 , 'Sydney Sixers'])
        except :
            count2 = count2
        count2 += 1
    count += 1
print(my_string)
print(new_string)