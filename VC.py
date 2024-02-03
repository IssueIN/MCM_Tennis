import pandas as pd
import matplotlib.pyplot as plt

# Load the match data
file_path = 'Wimbledon_featured_matches.csv'  # Adjust this to your file path
data = pd.read_csv(file_path)

# Calculate separate momentum for player 1 and player 2
momentum_window = 5  # Number of points to consider for calculating momentum
player1_momentum = [0]  # Initial momentum for player 1 is 0
player2_momentum = [0]  # Initial momentum for player 2 is 0

for i in range(1, len(data)):
    window_start = max(0, i - momentum_window)
    window_end = i
    points_in_window = data.iloc[window_start:window_end]
    total_points = len(points_in_window)
    player1_points_won = (points_in_window['point_victor'] == 1).sum()
    player2_points_won = (points_in_window['point_victor'] == 2).sum()
    player1_momentum_value = player1_points_won / total_points if total_points > 0 else 0
    player2_momentum_value = player2_points_won / total_points if total_points > 0 else 0
    player1_momentum.append(player1_momentum_value)
    player2_momentum.append(player2_momentum_value)

# Visualize separate momentum for player 1 and player 2
plt.figure(figsize=(12, 8))
plt.plot(player1_momentum, label='Player 1 Momentum')
plt.plot(player2_momentum, label='Player 2 Momentum', linestyle='--')
plt.xlabel('Point Number')
plt.ylabel('Momentum (Winning Rate in Last 5 Points)')
plt.title('Separate Momentum for Player 1 and Player 2 Over Time')
plt.legend()
plt.grid(True)
plt.show()

