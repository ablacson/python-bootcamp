def spend(expenses):
    """TODO: Add a new cost in expenses"""
    expense =int(input("Enter expense: "))
    current_expenses.append(expense)


def refund(expenses):
    """TODO: Remove the last cost added (if any)"""

    if expenses:
        expenses.pop(-1)
    else:
        print("No refund.")


def show(expenses):
    """TODO: Print the current list of expenses and total"""
    print("Current expenses:", expenses)
    print("Total expenses:", sum(expenses))

def save(expenses):
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(expense)

def main():
    running = True
    current_expenses = []

    while running:
        command = input("Command: ")
        if command == "spend":
            spend(current_expenses)

main()
