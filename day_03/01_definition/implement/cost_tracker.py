class CostTracker:

    def __init__(self):
     self.running = True
     self.expenses =[]

    def spend(self):
       new_expense = float("Enter new expense: ")
       self.expenses.append(new_expense)
       print(f"Added PHP {new_expense}")


    def refund(self):
        if self.expenses:
            refunded = self.expenses.pop(-1)
            print(f"Refunded PHP {refunded}")
        else:
            print("No expenses yet")

    def show(self):
        print(f"Expenses: (total PHP{sum(self.expenses)})")
        for number, expense in enumerate(self.expenses, start=1):
            print(f"\tExpense {number}:\tPHP {expense}")

    def main_loop(self):
        while self.running:
            command = input("Command: ")
            if command == "spend":
                self.spend()
            elif command == "refund":
                self.refund()
            elif command == "show":
                self.show()
            elif command == "exit":
                self.running = False

cost_tracker = CostTracker()
cost_tracker.main_loop()