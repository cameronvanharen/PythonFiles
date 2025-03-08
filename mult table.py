import math

table = []
num = input("enter a number: ")
num2 = int(num)
for i in range(1, 11):
    product = num2*i
    print(f"{num2} * {i} = {product}")
    table.append(product)

print(table)