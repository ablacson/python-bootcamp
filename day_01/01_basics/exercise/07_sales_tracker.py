# Ask the cost and pax or count for three separate items
item_cost_1 = int(input("Enter item cost:"))  # Let the user enter a number
item_count_1 = int(input("Enter the pax:")) # Let the user enter a number

item_cost_2 = int(input("Enter item cost:"))  # Let the user enter a number
item_count_2 = int(input("Enter item pax:"))  # Let the user enter a number

item_cost_3 = int(input("Enter item cost:"))  # Let the user enter a number
item_count_3 = int(input("Enter item pax:"))  # Let the user enter a number

# Calculate the total
total = (item_cost_1*item_count_1)+(item_cost_2*item_count_2)+(item_cost_3*item_count_3)
print(total)