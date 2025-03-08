class Restaurant:
    def __init__(self, menu_items, book_table, customer_orders):
        self.menu_items = menu_items
        self.book_table = book_table
        self.customer_orders = customer_orders

    def add_item_to_menu(item):
        item = input("FOOD: ")
        menu_items.append(item)
        print(menu_items)

    def book_tables(table):
        print(book_table)
        table = input("what table you want: ")
        book_table.append(table)

    def customer_order(order):
        print("Your order: " + customer_orders)
        item = input("Order: ")
        customer_orders.append(item)
        


menu_items = ["meat", "not meat", "fish"]
book_table = [""]
customer_orders = [""]
my_restaurant = Restaurant(menu_items, book_table, customer_orders)

my_restaurant.add_item_to_menu()
my_restaurant.book_tables()
my_restaurant.customer_order()