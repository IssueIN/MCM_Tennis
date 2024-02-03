import pandas as pd
from utils import read_csv_file, get_match_ids, get_player_names, convert_time_to_seconds
filename = 'Wimbledon_featured_matches.csv'

matches_df = read_csv_file(filename)
match_ids = get_match_ids(matches_df)
player_names = get_player_names(matches_df)
matches_df_seconds = convert_time_to_seconds(matches_df, 'elapsed_time')
