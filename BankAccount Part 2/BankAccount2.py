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






