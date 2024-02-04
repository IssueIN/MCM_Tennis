# Define the function to calculate the mental change due to winning or losing a match
# taking into account the athlete's historical win rate
def calculate_mental_change(win: bool, historical_win_rate: float) -> float:
    # Set the base change in mentality
    base_change = 1.0
    
    # Adjust the change based on the match outcome and historical win rate
    if win:
        # Positive change decreases as the historical win rate increases
        mental_change = base_change * (1 - historical_win_rate)
    else:
        # Negative change increases as the historical win rate increases
        mental_change = -base_change * (1 + historical_win_rate)
    
    return mental_change

# Example calculation with an athlete's historical win rate of 0.8
historical_win_rate_example = 0.8

# Calculate the mental change for winning a match
mental_change_win = calculate_mental_change(True, historical_win_rate_example)

# Calculate the mental change for losing a match
mental_change_lose = calculate_mental_change(False, historical_win_rate_example)

mental_change_win, mental_change_lose

print(mental_change_lose)