word = raw_input("Enter the word: ")

if word[::-1] == word:
 print word + " is a palindrome."
else:
 print word + " is not a palindrome."
