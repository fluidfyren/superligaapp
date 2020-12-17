# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 19:06:35 2020

@author: Lasse
"""

import pandas as pd
import pickle as pkl


def get_team_list(df):
    team_list = list(df['HomeTeam'].unique())
    return team_list


def create_teams_dict(df, team_list):    
    teams = {}
    for team in team_list:
        teams[team] = {}
        teams[team]['df'] = df[(df['HomeTeam'] == team) | (df['AwayTeam'] == team)]
        teams[team]['df'].reset_index(inplace=True, drop=True)
    return teams


def get_goals_and_points(teams):
    for team in teams:
        teams[team]['df']['Points'] = 0
        for i in range(len(teams[team]['df'])):                
            if teams[team]['df'].at[i,'HomeGoals'] > teams[team]['df'].at[i,'AwayGoals'] and teams[team]['df'].at[i, 'HomeTeam'] == team:
                teams[team]['df'].at[i,'Points'] = 3
            elif teams[team]['df'].at[i,'HomeGoals'] < teams[team]['df'].at[i,'AwayGoals'] and teams[team]['df'].at[i, 'HomeTeam'] == team:
                teams[team]['df'].at[i,'Points'] = 0
            elif teams[team]['df'].at[i,'HomeGoals'] > teams[team]['df'].at[i,'AwayGoals'] and teams[team]['df'].at[i, 'AwayTeam'] == team:
                teams[team]['df'].at[i,'Points'] = 0
            elif teams[team]['df'].at[i,'HomeGoals'] < teams[team]['df'].at[i,'AwayGoals'] and teams[team]['df'].at[i, 'AwayTeam'] == team:
                teams[team]['df'].at[i,'Points'] = 3
            else:
                teams[team]['df']['Points'][i] = 1
    return teams


def get_cumulative_points(teams):
    for team in teams:
        teams[team]['df']['Total Points'] = teams[team]['df']['Points'].cumsum()
        teams[team]['df']['Avg Points'] = teams[team]['df']['Points'].expanding().mean()
        teams[team]['df']['Shape'] = teams[team]['df']['Points'].rolling(3).mean()
    return teams


def get_opponents_points(teams, round_nr):
    for team in teams:
        for i in range(len(teams[team]['df'])):
            if teams[team]['df'].at[i,'HomeTeam'] == team:
                teams[team]['df'].at[i,'Opponent'] = teams[team]['df'].at[i,'AwayTeam']
            else:
                teams[team]['df'].at[i,'Opponent'] = teams[team]['df'].at[i,'HomeTeam']
        
            modstander = teams[team]['df'].at[i,'Opponent']
            if i < round_nr:
                teams[team]['df'].at[i,'Opponent avg points'] = teams[modstander]['df'].at[i,'Avg Points']
                teams[team]['df'].at[i,'Opponent Shape'] = teams[modstander]['df'].at[i,'Shape']
            else:
                teams[team]['df'].at[i,'Opponent avg points'] = teams[modstander]['df'].at[round_nr,'Avg Points']
                teams[team]['df'].at[i,'Opponent Shape'] = teams[modstander]['df'].at[round_nr,'Shape']
    return teams


def get_point_relation(teams):
    for team in teams:
        teams[team]['df']['Point_forhold'] = teams[team]['df']['Mean Points']/teams[team]['df']['Modstander Point']
    return teams

def pickle_teams(teams):
    for team in teams:
        f = open(f'data/teams/{team}.pkl', 'wb')
        pkl.dump(teams[team], f)
        f.close()

def give_colors(teams):
    colors = ['yellow', 'violet', 'tomato', 'teal', 'sienna', 'skyblue',
              'red', 'seagreen', 'navy', 'lime', 'lightsalmon', 'darkorchid']
    for i, team in enumerate(teams):
        teams[team]['color'] = colors[i]
    return teams


def combine_all(df):
    round_nr = df.dropna()['Round'].max()
    team_list = get_team_list(df)
    teams = create_teams_dict(df, team_list)
    teams = get_goals_and_points(teams)
    teams = get_cumulative_points(teams)
    teams = get_opponents_points(teams, round_nr)
    teams = give_colors(teams)
    pickle_teams(teams)
    return teams
    
if __name__ == "__main__":
    pass
            
