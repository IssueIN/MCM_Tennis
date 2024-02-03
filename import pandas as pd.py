import pandas as pd

# Load CSV file
file_name = 'Wimbledon_featured_matches.csv'  # Please replace with your file path
data = pd.read_csv(file_name)

# Count the number of times each player serves
server_counts = data['server'].value_counts()

# Calculate the probability of winning a point
point_winner_counts = data['point_victor'].value_counts()

# Count the number of times each player wins a point when serving
server_win_counts = data[data['server'] == data['point_victor']]['server'].value_counts()

# Calculate the probability of each player winning a point
total_points = len(data)
player1_win_probability = point_winner_counts[1] / total_points if 1 in point_winner_counts else 0
player2_win_probability = point_winner_counts[2] / total_points if 2 in point_winner_counts else 0

# Calculate the probability of each player winning a point while serving
player1_serve_win_probability = server_win_counts[1] / server_counts[1] if 1 in server_win_counts else 0
player2_serve_win_probability = server_win_counts[2] / server_counts[2] if 2 in server_win_counts else 0

# Print the results
print(f"Player 1 serves count: {server_counts[1] if 1 in server_counts else 0}")
print(f"Player 2 serves count: {server_counts[2] if 2 in server_counts else 0}")
print(f"Player 1 win probability: {player1_win_probability:.2%}")
print(f"Player 2 win probability: {player2_win_probability:.2%}")
print(f"Player 1 serve win probability: {player1_serve_win_probability:.2%}")
print(f"Player 2 serve win probability: {player2_serve_win_probability:.2%}")
