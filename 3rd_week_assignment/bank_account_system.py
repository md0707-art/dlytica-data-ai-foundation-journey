class BankAccount:

    def __init__(self, owner, opening_amount=0):
        self.owner = owner
        self.__balance = opening_amount

    # Getter Method
    def get_balance(self):
        return self.__balance

    # Protected Helper Method
    def _update_balance(self, amount):
        self.__balance += amount

    # Deposit Method
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self._update_balance(amount)
        print(f"Rs {amount} deposited successfully.")

    # Withdraw Method
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.__balance:
            print("Insufficient balance!")
            return

        self._update_balance(-amount)
        print(f"Rs {amount} withdrawn successfully.")


# Savings Account
class SavingsAccount(BankAccount):

    def __init__(self, owner, opening_amount=0):
        super().__init__(owner, opening_amount)

    def add_interest(self, rate):
        if rate <= 0:
            print("Interest rate must be positive.")
            return

        interest = self.get_balance() * rate / 100
        self.deposit(interest)

        print(f"Interest of {rate}% added.")


# Current Account
class CurrentAccount(BankAccount):

    def __init__(self, owner, opening_amount=0, overdraft_limit=0):
        super().__init__(owner, opening_amount)
        self.overdraft_limit = overdraft_limit

    # Method Overriding
    def withdraw(self, amount):

        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        new_balance = self.get_balance() - amount

        if new_balance < -self.overdraft_limit:
            print("Overdraft limit reached!")
            return

        self._update_balance(-amount)
        print(f"Rs {amount} withdrawn successfully.")


# -----------------------------
# Testing Savings Account
# -----------------------------

print("=" * 50)
print("SAVINGS ACCOUNT")
print("=" * 50)

s = SavingsAccount("Asha", 1000)

s.deposit(500)

s.add_interest(10)

print("Current Balance:", s.get_balance())

s.withdraw(5000)

print()


# -----------------------------
# Testing Current Account
# -----------------------------

print("=" * 50)
print("CURRENT ACCOUNT")
print("=" * 50)

c = CurrentAccount("Bibek", 200, overdraft_limit=500)

c.withdraw(600)

print("Current Balance:", c.get_balance())

c.withdraw(200)

print("Current Balance:", c.get_balance())