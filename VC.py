import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate simulated match data
np.random.seed(42)  # For consistency in results
points = 100  # Assuming the match has 100 points

# Probability of the server winning a point
prob_serve_win = 0.6
# Generate the outcome of each point, 1 for server win, 0 for receiver win
point_results = np.random.choice([1, 0], size=points, p=[prob_serve_win, 1-prob_serve_win])



# Step 2: Calculate momentum
# Calculate momentum based on the last 5 points
momentum_window = 5
momentum = [0]  # Initial momentum is 0
for i in range(1, points):
    # Calculate momentum within the last 5 points (server wins - receiver wins)
    window_start = max(0, i-momentum_window)
    window_end = i
    window_momentum = point_results[window_start:window_end].sum() - (momentum_window - point_results[window_start:window_end].sum())
    momentum.append(window_momentum)



# Step 3: Visualize match momentum
plt.figure(figsize=(10, 6))
plt.plot(momentum, label='Match Momentum')
plt.xlabel('Point Number')
plt.ylabel('Momentum')
plt.title('Match Momentum Over Time')
plt.legend()
plt.grid(True)
plt.show()
