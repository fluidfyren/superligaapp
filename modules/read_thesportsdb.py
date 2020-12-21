# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 21:57:11 2020

@author: Lasse
"""
import pandas as pd
import requests

leagues = {'Superligaen':'4340','Premier League':'4328', 'Bundesliga':'4331',
           'La Liga':'4335', 'Serie A':"4334"}

def read_from_thesportsdb(league_id='4340'):
    url = f'https://www.thesportsdb.com/api/v1/json/4013017/eventsseason.php?id={league_id}&s=2020-2021'

    response = requests.request("GET", url)
    print(response)
    text = response.text

    df = pd.read_json(text)

    matches = []

    for index, row in df.iterrows():
        matches.append(row[0])
    

    df_new = pd.DataFrame(columns=['Round', 'HomeTeam', 'AwayTeam', 'HomeGoals', 'AwayGoals', 'Date'])

    for i, match in enumerate(matches):
        df_new = df_new.append({'Round':pd.to_numeric(match['intRound']),
                            'HomeTeam':match['strHomeTeam'],
                            'AwayTeam':match['strAwayTeam'],
                            'HomeGoals':pd.to_numeric(match['intHomeScore']),
                            'AwayGoals':pd.to_numeric(match['intAwayScore']),
                            'Date':match['dateEvent']
                            }, 
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

def read_from_match(match_id):
    url = f'https://www.thesportsdb.com/api/v1/json/4013017/lookuptimeline.php?id={match_id}'

    response = requests.request("GET", url)
    print(response)
    text = response.text
    if text != '{"timeline":null}':
        text = pd.read_json(text)
        
        events = []
        for index, row in text.iterrows():
            events.append(row[0])
        return events
    return text

if __name__ == "__main__":
    #df_new = read_from_thesportsdb(league_id='4328')
    #round_nr = df_new.dropna()['round()d'].max()
    df = read_from_thesportsdb_players(league_id='4328')
    df_match = read_from_match('1032737')
