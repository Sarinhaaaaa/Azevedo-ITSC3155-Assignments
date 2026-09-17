class BankAccount:
    bank_title = "Bank of America"
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number
        self.__routing_number = routing_number


    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"Deposited ${amount:.2f}. New Balance: {self.current_balance}")
        else:
            print("Deposit amount must be greater than 0")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount must be greater than 0")
            return

        remaining_balance = self.current_balance - amount

        if remaining_balance < self.minimum_balance:
            print("Transaction denied. Remaining balance dropped below Minimum Balance")
        else:
            self.current_balance -= amount
            print("Withdrawal successful")

    def print_customer_information(self):
        print(f"Bank title: {self.bank_title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: {self.current_balance}")
        print(f"Minimum Balance: {self.minimum_balance}")

print("Account 1 Test:")
account1 = BankAccount("Sarah", 500.0,100.0)
account1.print_customer_information()
account1.deposit(200.0)
account1.withdraw(150.0)
account1.withdraw(500.0)

print("Account 2 Test:")
account2 = BankAccount("Chloe", 1500.0,250.0)
account2.print_customer_information()
account2.withdraw(1200.0)
account2.withdraw(100)



