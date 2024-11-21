def factorial(n):
    """Calculate the factorial of n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def combination(n, r):
    """Calculate the number of combinations C(n, r)."""
    if n < r:
        return "Error: n must be greater than or equal to r"
    return factorial(n) // (factorial(r) * factorial(n - r))

# List of (n, r) pairs to calculate combinations
pairs = [(6, 2), (8, 3), (10, 4), (12, 5), (15, 7)]

# Calculate and display results
print("Combinations for given (n, r) pairs:")
for n, r in pairs:
    result = combination(n, r)
    print(f"C({n}, {r}) = {result}")
