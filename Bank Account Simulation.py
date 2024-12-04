class BankAccount:
    def __init__(self, account_holder):
        """
        Initialize the bank account with an account holder's name and a zero balance.
        """
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """
        Deposit the specified amount into the account.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount:.2f} to {self.account_holder}'s account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account if sufficient funds are available.
        """
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount:.2f} from {self.account_holder}'s account.")
        else:
            print("Insufficient funds. Withdrawal denied.")

    def view_balance(self):
        """
        Display the current balance of the account.
        """
        print(f"{self.account_holder}'s account balance: ₹{self.balance:.2f}")

# Example Usage
# Create an account
account = BankAccount("John Doe")

# Deposit money
account.deposit(5000)
account.deposit(1500)

# View balance
account.view_balance()

# Withdraw money
account.withdraw(2000)
account.withdraw(10000)  # Attempt to withdraw more than balance

# View balance after transactions
account.view_balance()
