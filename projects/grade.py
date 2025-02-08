# Define the data
grades_and_credits = [
    (22, 3.90),
    (25, 3.71),
    (23, 3.78),
    (21, 3.69),
    (20, 3.93),
    (16, 3.80),
    (24, 3.97),
]

# Calculate the total weighted sum of grades and total credits
total_weighted_sum = sum(credits * grade for credits, grade in grades_and_credits)
total_credits = sum(credits for credits, grade in grades_and_credits)

# Calculate the weighted average
weighted_average = total_weighted_sum / total_credits
print(total_weighted_sum, total_credits, weighted_average)
