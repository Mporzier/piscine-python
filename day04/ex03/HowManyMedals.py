from FileLoader import FileLoader
import pandas


def howManyMedals(data, name):
    matchAthlete = data.loc[data['Name'] == name]
    if matchAthlete.empty:
        print("No information about this athlete.")
        return None
    matchAthlete = matchAthlete.dropna(subset=['Medal'])
    if matchAthlete.empty:
        print("This athlete didn't get any medal.")
        return None
    print(matchAthlete)
    dicts = {}
    for index, row in matchAthlete.iterrows():
        if row['Year'] not in dicts:
            dicts[row['Year']] = {'G': 0, 'S': 0, 'B': 0}
        dicts[row['Year']][row['Medal'][0]
                           ] = dicts[row['Year']][row['Medal'][0]] + 1
    return dicts
