# Program to check if a string is palindrome or not
import time

print("Let's see if your word is a palindrome!")
time.sleep(1)

# Ask user to input word
word = input('Enter a word: ').casefold()  # casefold() ignores casing
print("...")
time.sleep(1)

# reverse the string
reverse_word = reversed(word)

# check if the string is equal to its reverse
if list(word) == list(reverse_word):
    print("This is a Palindrome!")
else:
    print("This is not a Palindrome!")
