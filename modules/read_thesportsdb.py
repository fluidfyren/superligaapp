# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 21:57:11 2020

@author: Lasse
"""
import pandas as pd
import requests

leagues = {'Superligaen':'4340','Premier League':'4328', 'Bundesliga':'4331',
           'La Liga':'4335'}

def read_from_thesportsdb(league_id='4340'):
    url = f'https://www.thesportsdb.com/api/v1/json/4013017/eventsseason.php?id={league_id}&s=2020-2021'

    response = requests.request("GET", url)
    print(response)
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

    
def read_from_thesportsdb_players(league_id='4340'):
    url = f'https://www.thesportsdb.com/api/v1/json/4013017/eventsseason.php?id={league_id}&s=2020-2021'

    response = requests.request("GET", url)
    print(response)
    text = response.text

    df = pd.read_json(text)
    
    matches = []

    for index, row in df.iterrows():
        matches.append(row[0])
    
    return matches



if __name__ == "__main__":
    #df_new = read_from_thesportsdb(league_id='4328')
    #round_nr = df_new.dropna()['Round'].max()
    df = read_from_thesportsdb_players(league_id='4328')