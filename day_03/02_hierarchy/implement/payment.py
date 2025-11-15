class CashPayment:
    def __init__(self, amount):
        self.amount = amount

    def total(self):
        return self.amount


class CreditPayment:
    def __init__(self, amount, limit="50_000"):
        """Set attributes here"""
        self.limit = limit

    def total(self):
        if self.amount > self.limit:
            raise ValueError("Amount must be greater than or equal to limit")
        raise ValueError

class OnlinePayment:
    def __init__(self, amount, fee):
        """Set attributes here"""
        self.amount = amount
        self.fee = fee

    def total(self):
        """Return amount + fee"""
        return self.amount + self.fee


class DiscountedPayment:
    def __init__(self, amount=5_000, discount=0.5):
        """Set attributes here"""
        self.amount = amount
        self.discount = float(discount)

    def total(self):
        """Return amount - discount"""
        return self.amount - self.discount

payments = [
    CashPayment(1_000),
    CashPayment(10_000),
    CashPayment(1_000)
]

for payment in payments:
    print(payment.total())
