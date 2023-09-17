class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"${amount} deposited successfully."
        else:
            return "Invalid deposit amount. Amount must be greater than 0."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"${amount} withdrawn successfully."
        else:
            return "Invalid withdrawal amount or insufficient balance."

    def display_balance(self):
        return f"Account balance for {self.__account_holder_name} (Account #: {self.__account_number}): ${self.__account_balance}"


# Test the BankAccount class
if __name__ == "__main__":
    # Create an instance of BankAccount
    account = BankAccount("12345", "John Doe", 1000)

    # Display initial balance
    print(account.display_balance())

    # Deposit money
    print(account.deposit(500))

    # Withdraw money
    print(account.withdraw(200))

    # Display updated balance
    print(account.display_balance())