# TODO: Fill in the details of the item you plan to buy
order = {
    "Name": "Memory",
    "Info": "4TB",
    "Price": 2_000,
    "Discount": False
}

# TODO: Print the item details in the following format:
"""
Order:
	Name: item name
	Info: item info
	...
"""
print("Order:")
for fields, details in order.items():
    print(f"{fields}: {details}")
