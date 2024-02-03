import pandas as pd
from params import matches_df_seconds, match_ids, player_names

def fetch_matches_by_matches_id(df, match_id):
  match_df = df[df['match_id'] == match_id]
  return match_df

def fetch_match_ids_by_player(df, player_name):
  filtered_matches_df = df.loc[(df['player1'] == player_name) | (df['player2'] == player_name)]
  ids = filtered_matches_df['match_id'].unique()
  return ids

def save_matches_by_id_to_csv(df, match_ids):
  for match_id in match_ids:
    match_df = fetch_matches_by_matches_id(df, match_id)
    match_df.to_csv(f'output/matches_data/{match_id}.csv', index=False)

def save_players_in_matches_to_csv(df, match_ids):
  players_in_matches = []
  for match_id in match_ids:
    match_df = fetch_matches_by_matches_id(df, match_id)
    players = match_df[['player1', 'player2']].iloc[0].tolist()
    players_in_matches.append([match_id] + players)
    
    players_df = pd.DataFrame(players_in_matches, columns=['match_id', 'player1', 'player2'])
    players_df.to_csv('output/players_in_matches.csv', index=False)

def save_player_names_to_csv(player_names):
  players_df = pd.DataFrame(player_names, columns=['players'])
  players_df.to_csv('output/player_names.csv', index=False)


save_players_in_matches_to_csv(matches_df_seconds, match_ids)
save_matches_by_id_to_csv(matches_df_seconds, match_ids)
save_player_names_to_csv(player_names)