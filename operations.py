def add(a,b):
    x = a + b
    return x
def subtract(a,b):
    x = a - b
    return x
def multiply(a,b):
    x = a * b
    return x
def divide(a,b):
    x = a / b
    return x

print("Choose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Divison")
choice = input("Select operation: ")
a = int(input("first number: "))
b = int(input("second number: "))
if choice == "1":
    x = add(a,b)
    print(x)
elif choice == "2":
    x = subtract(a,b)
    print(x)
elif choice == "3": 
    x = multiply(a,b)
    print(x)
elif choice == "4":
    x = divide(a,b)
    print(x)