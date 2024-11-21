# Define the two sets
avaya_set = {'Giri', 'Vani', 'Vasavi', 'Rohith', 'Teena'}
pindrop_set = {'Soundarya', 'Sukeerthi', 'Prathyusha', 'Gowthami'}

# Calculate the intersection (common names in both sets)
intersection = avaya_set.intersection(pindrop_set)

# Check if there are any common names and print accordingly
if intersection:
    print("Names in both Avaya and Pindrop:", intersection)
else:
    print("No one")
