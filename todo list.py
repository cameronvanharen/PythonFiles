def add(obj):
    list.append(obj)

def remove(num):
    list.remove[num]

list = ["uno", "dos", "tres"]
while True:
    print(list)
    choice = input("add or remove task: ")

    if choice == "add":
        thing = input("add task: ")
        add(thing)
    if choice == "remove":
        thing = input("remove task #: ")
        remove(thing)