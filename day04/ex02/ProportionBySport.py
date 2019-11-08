from FileLoader import FileLoader
import pandas


def proportionBySport(data, year, sport, sex):
    matchYear = data.loc[data['Year'] == year]
    if matchYear.empty:
        print("No information about this year.")
        return None
    matchSex = matchYear.loc[matchYear['Sex'] == sex]
    if matchSex.empty:
        print("No information about this gender.")
        return None
    matchSex = matchSex.drop_duplicates(
        subset=["Name"], keep='first')
    matchSport = matchSex.loc[matchSex['Sport'] == sport]
    if matchSport.empty:
        print("No information about this sport.")
        return None
    numberPerSex = matchSex.shape[0]
    numberAthletes = matchSport.shape[0]
    proportion = numberAthletes / numberPerSex
    return proportion
