total = 1
running = True
while running:
    command = input("Provide command: ")

    if command == "add":
        number = int(input("Input Number: "))
        total = number+total
        print("The Total is:", total)
        pass
    if command == "sub":
        number = int(input("Input Number: "))
        total = total-number
        print("The Total is:", total)
        pass
    elif command == "exit":
        running = False
