"""
    TODO: Create a function `line_generator` that has a parameter `number` and prints the following:
	Line 1
	Line 2
	...
	Line number
"""

# TODO: Use the function once

def line_generator(number):
    for line in range(number): #This item gets repeated
        print("Line",number+1)

line_generator(19)