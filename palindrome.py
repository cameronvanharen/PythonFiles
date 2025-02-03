word = input("Input word: ")
letters = list(word)

wordBackwards = ""

for i in word: 
    wordBackwards = i + wordBackwards 

if word == wordBackwards:
    print("word is a palindrome")
else:
    print("word is not a palindrome")

 
