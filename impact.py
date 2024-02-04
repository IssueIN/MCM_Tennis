def calculate_mental_impact(win_rate, match_result):
    # Define the mindset impact factors; you can adjust them as needed
    positive_impact_factor = 0.2  # Positive mindset impact factor
    negative_impact_factor = 0.4  # Negative mindset impact factor

    # Calculate positive and negative mindset changes
    if match_result == "win":
        positive_change = win_rate * positive_impact_factor
        negative_change = (1 - win_rate) * negative_impact_factor
    elif match_result == "lose":
        positive_change = (1 - win_rate) * positive_impact_factor
        negative_change = win_rate * negative_impact_factor
    else:
        # If the match result is not "win" or "lose," return 0
        return 0

    # Calculate the total mindset impact
    total_mental_impact = positive_change - negative_change

    return total_mental_impact

# Example usage
win_rate = 0.7  # Player's historical win rate
match_result = "win"  # Match result, can be "win" or "lose"
mental_impact = calculate_mental_impact(win_rate, match_result)
print(f"Mental Impact Value: {mental_impact}")
