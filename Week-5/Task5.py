class BankAccount:
    def __init__(self, owner, initial_balance=0):
        # Private attributes denoted by double underscores
        self.__owner = owner
        self.__balance = initial_balance

    def deposit(self, amount):
        # Adds money to the balance if the amount is positive.
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.__balance}")
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        # Subtracts money if amount is positive and does not exceed balance.
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print(f"Error: Insufficient funds. Current balance: ${self.__balance}")
        else:
            self.__balance -= amount
            print(f"Withdrew: ${amount}. Remaining balance: ${self.__balance}")

    def get_balance(self):
        # Public method to safely view the private balance.
        return self.__balance


if __name__ == "__main__":
    account = BankAccount("John Doe", 100)
    
    # Successful transactions
    account.deposit(50)
    account.withdraw(30)
    
    # Testing Validation
    print("\n--- Testing Validation ---")
    account.deposit(-10)        # Should trigger "must be positive" error
    account.withdraw(200)       # Should trigger "insufficient funds" error
    
    print(f"\nFinal Balance: ${account.get_balance()}")