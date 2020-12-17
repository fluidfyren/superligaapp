# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 16:42:26 2020

@author: Lasse
"""
import sqlite3
import read_thesportsdb, combine_data
import pandas as pd

conn = sqlite3.connect('superliga.db')
c = conn.cursor()

teams = read_thesportsdb.read_from_thesportsdb()
teams, round_nr = combine_data.combine_all(teams)

for team in teams:
    teams[team]['df'].to_sql(f'{team}', conn, if_exists='replace', index = False)


dataframes = []
for team in teams:
    dataframes.append(pd.read_sql_query(f"SELECT * FROM '{team}'", conn))

#c.execute(''' 
#          SELECT name FROM sqlite_master WHERE type="table"''')

#for row in c.fetchall():
#    print (row)