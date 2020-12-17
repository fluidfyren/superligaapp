from modules import read_thesportsdb, combine_data


df = read_thesportsdb.read_from_thesportsdb()
teams = combine_data.combine_all(df)
team_list = list(teams.keys())