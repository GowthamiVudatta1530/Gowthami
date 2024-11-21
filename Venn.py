# Define sets for the types of flowers
red_flowers = {'rose', 'tulip', 'lily', 'marigold'}
fragrant_flowers = {'rose', 'jasmine', 'lavender', 'lily'}

# Calculate set operations
both_red_and_fragrant = red_flowers.intersection(fragrant_flowers)
only_red = red_flowers - fragrant_flowers
only_fragrant = fragrant_flowers - red_flowers
all_flowers = red_flowers.union(fragrant_flowers)

# Print the results
print("Flowers that are both red and fragrant:", both_red_and_fragrant)
print("Flowers that are only red:", only_red)
print("Flowers that are only fragrant:", only_fragrant)
print("All flowers (union of both sets):", all_flowers)
