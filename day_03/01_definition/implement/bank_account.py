class BankAccount:
    def __init__(self, initial_balance =100):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance+= amount

    def withdraw(self, amount):
        self.balance-= amount

    def print_balance(self):
        print(self.balance)