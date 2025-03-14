import csv

# Define flashcard data for cognitive biases in English
cognitive_bias_flashcards = [
    ["Question", "Answer"],
    ["What is Functional Fixedness?", "Functional Fixedness is a cognitive bias where a person only sees an object for its traditional use. Example: Seeing a hammer only for driving nails and not as a weight. Real-life example: Struggling to use a shoe as a hammer in emergencies."],
    ["What is a Mental Set?", "A Mental Set is the tendency to approach problems in a certain way because it worked in the past. Example: A child solving a puzzle the same way each time. Real-life example: Using the same troubleshooting method for computer issues, even when the problem is different."],
    ["What is Confirmation Bias?", "Confirmation Bias is the tendency to favor information that supports existing beliefs and ignore contradictory evidence. Example: Believing a diet works and ignoring studies showing it doesn't. Real-life example: A person only watching news channels that align with their political views."],
    ["What is Anchoring Bias?", "Anchoring Bias is relying too heavily on the first piece of information received. Example: Thinking a $50 shirt is cheap after seeing a $100 one. Real-life example: Buying a house based on its initial listed price without assessing market value."],
    ["What is Cognitive Inertia?", "Cognitive Inertia is sticking to existing thought patterns even when new evidence contradicts them. Example: Refusing to believe new research that challenges old ideas. Real-life example: An employee resisting a new software update because they're used to the old one."],
    ["What is Hindsight Bias?", "Hindsight Bias is the tendency to see events as predictable after they occur. Example: Claiming 'I knew it!' after a surprise happens. Real-life example: Saying you 'knew' a stock would crash after it already did."],
    ["What is the Law of the Instrument?", "The Law of the Instrument is using a familiar tool for all problems, even when it's inappropriate. Example: Solving every coding problem with one programming language. Real-life example: A consultant applying the same strategy to every client, regardless of suitability."]
]

# Save the flashcards to a CSV file
file_path_biases = 'Cognitive_Bias_Flashcards.csv'  # Saves the file in the current working directory
with open(file_path_biases, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(cognitive_bias_flashcards)

print(f"File saved successfully as {file_path_biases}")
