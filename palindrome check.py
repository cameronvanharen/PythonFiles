def is_palindrome(word):
    palindrome = True
    check = True
    i = 0
    for j in word:
        if word[len(word)-i] == word[i]:
            check = True
        else:
            check = False
        
        if check == False:
            palindrome = False
        i = i -1    
    print(palindrome)
    

is_palindrome("fafaf")


    


