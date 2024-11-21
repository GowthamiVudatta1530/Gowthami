# Number of boys and girls
num_boys = 3
num_girls = 2

# Calculate factorial for arrangements
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

# Calculate boys arrangements (3!)
boys_arrangements = factorial(num_boys)

# Calculate girls arrangements (2!)
girls_arrangements = factorial(num_girls)

# Total possible arrangements (3! × 2!)
total_arrangements = boys_arrangements * girls_arrangements

print(f"Number of boys: {num_boys}")
print(f"Number of girls: {num_girls}")
print(f"Boys arrangements (3!): {boys_arrangements}")
print(f"Girls arrangements (2!): {girls_arrangements}")
print(f"Total possible arrangements: {total_arrangements}")