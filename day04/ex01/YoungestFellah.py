from FileLoader import FileLoader
import pandas


def youngestFellah(data, year):
    matchYear = data.loc[data['Year'] == year]
    if matchYear.empty:
        print("No information about this year.")
        return None
    females = matchYear.loc[data["Sex"] == 'F']
    males = matchYear.loc[data["Sex"] == 'M']
    ageYoungestF = int(females.nsmallest(1, 'Age').values[0][3])
    ageYoungestM = int(males.nsmallest(1, 'Age').values[0][3])
    dict = {
        "f":ageYoungestF,
        "m":ageYoungestM
    }
    return dict
