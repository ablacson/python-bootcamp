prices = [10_000, 20, 3_000, 3, -200, 1_000]

# TODO: Print the first, third, and last item
print("Current Price:"[0])
print("Current Price:"[2])
print("Current Price:"[-1])

# TODO: Change the first, third, and last values to half the price
indices = [0, 2, -1]
for index in indices:
    prices[index]//=2

# TODO: Print the first, third, and last item again to see new price
print("New Price:"[0])
print("New Price:"[2])
print("New Price:"[-1])
