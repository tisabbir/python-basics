def is_palindrome(word):
    word = word.lower()  # Convert to lowercase to make it case-insensitive
    return word == word[::-1]  # Compare the string with its reverse

# Example Usage
word = "Madam"
if is_palindrome(word):
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome.")
