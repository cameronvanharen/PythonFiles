movie1 = input("Favorite movie #1: ")
movie2 = input("Favorite movie #2: ")
movie3 = input("Favorite movie #3: ")
movie4 = input("Favorite movie #4: ")
movie5 = input("Favorite movie #5: ")

Movies = [movie1, movie2, movie3, movie4, movie5]
index = 4

print("Your favorite movies in reverse: ")
while index >= 0:
    print(Movies[index])
    index -= 1
