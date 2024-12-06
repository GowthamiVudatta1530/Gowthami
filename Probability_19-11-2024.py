
# Total number of balls
total_balls = 30

# Number of red balls
red_balls = 12

# Calculate probability of NOT picking a red ball
non_red_probability = (total_balls - red_balls) / total_balls

print(f"Total balls: {total_balls}")
print(f"Red balls: {red_balls}")
print(f"Probability of picking a non-red ball: {non_red_probability}")
print(f"Probability as percentage: {non_red_probability * 100}%")
