items = ["rice", "noodles", "toyo", "spam", "coffee"]

item_to_find = "spam"
item_found = False

for item in items:
    if item == item_to_find:
        item_found = True
        break
print(item_found)
