# Number of members for each activity
painting_members = 40  # Set A
dancing_members = 50   # Set B
both_activities = 20   # A ∩ B

# Calculate total members using addition rule
# Total = A + B - (A ∩ B)
total_members = painting_members + dancing_members - both_activities

print(f"Members who paint: {painting_members}")
print(f"Members who dance: {dancing_members}")
print(f"Members who do both: {both_activities}")
print(f"Total members who paint OR dance: {total_members}")