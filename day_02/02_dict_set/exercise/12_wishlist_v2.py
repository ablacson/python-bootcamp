# TODO: Fill in the details of the items you plan to buy
wishlist = {
    "Item1":
        {
        "Name": "Item1",
        "Info": "4TB",
        "Price": 2_000,
        "Discount": False
    },
    "Item2":{
        "Name": "Item2",
        "Info": "Red",
        "Price": 2_000,
        "Discount": False
    },
    "Item3":{
        "Name": "Item3",
        "Info": "Blue",
        "Price": 2_000,
        "Discount": False
    }
}

# TODO: Print the item details in the following format (for each order):
"""
Order:
	Name: item name
	Info: item info
	...
"""
print("Wishlist:")
for fields, details in wishlist.items():
    print(f"\t{fields}: {details['Info']}")


