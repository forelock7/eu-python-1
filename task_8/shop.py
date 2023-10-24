class Shop():
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0
    def describe_shop(self):
        print(f"'{self.shop_name}' ({self.store_type})")
    def open_shop(self):
        print(f"Online shop '{self.shop_name}' is open")
    def set_number_of_units(self, number_of_units):
        self.number_of_units = number_of_units
    def increment_number_of_units(self, number):
        self.number_of_units += number

class Discount(Shop):
    def __init__(self, shop_name, store_type, discount_products):
        super().__init__(shop_name, store_type)
        self.discount_products = discount_products
    def get_discounts_ptoducts(self):
        print(f"Products: {self.discount_products}")

# Task 8.1a
print("*** Task 8.1a ***")
store = Shop('Silpo', 'grocery store')
print(store.shop_name)
print(store.store_type)
store.open_shop()
store.describe_shop()
# Task 8.1b
print("*** Task 8.1b ***")
store2 = Shop('Fora', 'grocery store')
store3 = Shop('Foxtrot', 'electronics store')
store4 = Shop('OLX', 'marketplace')
store2.describe_shop()
store3.describe_shop()
store4.describe_shop()
# Task 8.1c
print("*** Task 8.1c ***")
store_c = Shop('Silpo', 'grocery store')
print("number_of_units =", store_c.number_of_units)
store_c.number_of_units = 5
print("number_of_units =", store_c.number_of_units)
# Task 8.1d
print("*** Task 8.1d ***")
store_c.set_number_of_units(77)
print("number_of_units =", store_c.number_of_units)
store_c.increment_number_of_units(11)
print("number_of_units =", store_c.number_of_units)
# Task 8.1e
print("*** Task 8.1e ***")
store_discount = Discount('Foxtrot', 'electronics store', ['Iphone', 'Apple Watch', 'Ipad'])
store_discount.get_discounts_ptoducts()