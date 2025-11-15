class NegativeDep(ValueError):
    def __init__(self):
        super().__init__("Negative Deposit.")
class Over(ValueError):
    def __init__(self):
        super().__init__("Over withdrawn.")


class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):
        self._balance += amount
        if amount < 0:
            raise NegativeDep()

    def withdraw(self, amount):
        if amount < 0:
            if amount > self._balance:
                raise Over

        self._balance -= amount

    def print_balance(self):
        print(self._balance)


bank_account = BankAccount()
