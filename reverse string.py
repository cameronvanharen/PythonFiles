str = input("enter string: ")
x = len(str) - 1
for i in range(len(str)):
    char = str[x]
    newstr = newstr + char
    print(newstr)