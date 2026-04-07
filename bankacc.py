class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.balance = initial_balance
        self.transactions = []
        
        # record initial deposit
        self.transactions.append(f"Account created with balance: {initial_balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: {amount}")
            print(f"{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            self.transactions.append(f"Failed withdrawal attempt: {amount}")
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
            print(f"{amount} withdrawn successfully.")

    def get_balance(self):
        return self.balance

    def get_statement(self):
        print("\nTransaction Statement:")
        for t in self.transactions:
            print(t)

## create object
acc = BankAccount("Swetank", 1000)

# perform operations
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)

# print balance
print("Current Balance:", acc.get_balance())

# print statement
acc.get_statement()