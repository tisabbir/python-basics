# Generate all possible pairs of numbers from 1 to 8
pairs = [(i, j) for i in range(1, 9) for j in range(1, 9)]

# Print the pairs
for pair in pairs:
    print(pair)
