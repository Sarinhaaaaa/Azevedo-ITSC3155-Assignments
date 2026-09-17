from BankAccount2 import BankAccount
class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit

    def transfer(self, amount, target_account):
        if amount > self.transfer_limit:
            print(f"Transfer denied. Exceeds transfer limit of ${self.transfer_limit:.2f}")
            return

        if amount <= 0:
            print("Transfer amount must be greater than 0")
            return

        remaining_balance = self.current_balance - amount

        if remaining_balance < self.minimum_balance:
            print("Transaction denied. Remaining balance dropped below Minimum Balance")
        else:
            self.current_balance -= amount
            target_account.deposit(amount)
            print(f"Successfully transferred ${amount:.2f} to {target_account.customer_name}.")