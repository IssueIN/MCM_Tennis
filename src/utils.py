import numpy as np
import pandas as pd

def filepath_with_filename(filename):
  filepath = 'data/' + filename
  return filepath

def read_csv_file(filename):
  try:
    df = pd.read_csv(filepath_with_filename(filename))
    return df
  except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    return None

def get_match_ids(df):
  ids = df['match_id'].unique()
  return ids

def get_player_names(df):
  all_players = pd.concat([df['player1'], df['player2']])
  names = all_players.unique()
  return names

def convert_time_to_seconds(df, column_name):
  df[column_name] = pd.to_timedelta(df[column_name])
  df[column_name] = df[column_name].dt.total_seconds()
  return df






  
