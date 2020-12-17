# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 21:57:11 2020

@author: Lasse
"""
import pandas as pd
import requests
from modules import combine_data

def read_from_thesportsdb():
    url = 'https://www.thesportsdb.com/api/v1/json/1/eventsseason.php?id=4340&s=2020-2021'

    response = requests.request("GET", url)
    text = response.text

    df = pd.read_json(text)

    matches = []

    for index, row in df.iterrows():
        matches.append(row[0])
    

    df_new = pd.DataFrame(columns=['Round', 'HomeTeam', 'AwayTeam', 'HomeGoals', 'AwayGoals'])

    for i, match in enumerate(matches):
        df_new = df_new.append({'Round':pd.to_numeric(match['intRound']),
                            'HomeTeam':match['strHomeTeam'],
                            'AwayTeam':match['strAwayTeam'],
                            'HomeGoals':pd.to_numeric(match['intHomeScore']),
                            'AwayGoals':pd.to_numeric(match['intAwayScore'])}, 
                           ignore_index=True)

    return df_new

if __name__ == "__main__":
    df_new = read_from_thesportsdb()
    round_nr = df_new.dropna()['Round'].max()