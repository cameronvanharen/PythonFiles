def is_palindrome(word):

   for i in range(0, len(word)-1):
      if word[i] != word[len(word) - 1 - i]:
         return False
    
   return True

print(is_palindrome("not true"))