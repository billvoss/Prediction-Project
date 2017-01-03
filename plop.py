import pandas as pd

teamDF = pd.read_csv('BBLTeams.csv')
batDF = pd.read_csv('BattingData.csv')
bowlDF = pd.read_csv('BowlingData.csv')

print(batDF)

bowlDF.set_index('Name', inplace = 'true')
batDF.set_index('Name', inplace = 'true')

print(batDF)
