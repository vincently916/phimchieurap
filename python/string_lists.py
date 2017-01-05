word = raw_input("Enter the word: ")
new_word = ""
counter = len(word) - 1
while counter  >= 0:
  new_word = new_word + (word[counter])
  counter -= 1

if new_word == word:
 print word + " is a palindrome."
