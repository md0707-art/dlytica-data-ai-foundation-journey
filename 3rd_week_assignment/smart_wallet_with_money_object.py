class Money:

    def __init__(self, amount, currency="Rs"):
        self.amount = amount
        self.currency = currency

    # Human-readable format
    def __str__(self):
        return f"{self.currency} {self.amount}"

    # Developer-friendly format
    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"

    # Addition Operator (+)
    def __add__(self, other):
        return Money(self.amount + other.amount, self.currency)

    # Equality Operator (==)
    def __eq__(self, other):
        return self.amount == other.amount

    # Less Than Operator (<)
    def __lt__(self, other):
        return self.amount < other.amount


class Wallet:

    def __init__(self, notes):
        self.notes = notes

    # len(wallet)
    def __len__(self):
        return len(self.notes)

    # Total Money in Wallet
    def total(self):

        total_money = Money(0)

        for note in self.notes:
            total_money = total_money + note

        return total_money


# --------------------------------
# Testing Money Class
# --------------------------------

print("=" * 50)
print("MONEY OBJECTS")
print("=" * 50)

a = Money(500)
b = Money(300)

print("a =", a)
print("b =", b)

print("\na + b =", a + b)

print("a == Money(500) :", a == Money(500))

print("b < a :", b < a)

# Sorting
notes = [Money(100), Money(500), Money(50)]

print("\nBefore Sorting:")
print(notes)

print("\nAfter Sorting:")
print(sorted(notes))

# --------------------------------
# Testing Wallet Class
# --------------------------------

print("\n" + "=" * 50)
print("WALLET")
print("=" * 50)

wallet = Wallet(notes)

print("Number of Notes:", len(wallet))

print("Total Amount:", wallet.total())