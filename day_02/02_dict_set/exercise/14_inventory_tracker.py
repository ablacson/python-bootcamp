def add(inventory):
    """TODO:
        Ask for item name, info, and stock
        Create a dictionary with key: name, info, stock
        Add that dictionary to inventory
    """
    name = input("Item name: ")
    info = input("Item info: ")
    stock = int(input("Item stock: "))

    item = {
        "name": name,
        "info": info,
        "stock": stock,

    }

    inventory.append(item)


def remove(inventory):
    """TODO:
        Ask for item index (int)
        Remove item in that index in inventory
    """
    index=int(input("Item index: "))
    inventory.pop(index)

def read(inventory):
    """TODO:
        Ask for item index (int)
                Show item in that index in inventory
    """
    index=int(input("Item index: "))
    print(inventory[index])


def show(inventory):
    """TODO: Print items line-by-line"""
def print_item(item):
    for field, details in item.items():
        print(f"{field}: {details}")


def main():
    """Created to test functions"""
    running = True
    item_detail = str | int | float
    inventory: list[dict[str, item_detail]] = []

    while running:
        command = input("Command: ")
        if command == "add":
            # TODO: Use add command"""
            add(inventory)
        elif command == "remove":
            #  TODO: Use remove command"""
            remove(inventory)
        elif command == "read":
            # TODO: Use read command"""
            read(inventory)
        elif command == "show":
            # TODO: Use show command"""
            show(inventory)
        elif command == "exit":
            running = False


main()
