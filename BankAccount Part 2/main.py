from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount

print("Creating Accounts...")
savings_acct1 = SavingsAccount("Sarah", 1000.0, 100.0, 1001, 123456789, 0.05)
savings_acct2 = SavingsAccount("Maddy", 500.0, 50.0, 1002, 123456789, 0.02)

checking_acct1 = CheckingAccount("Charlie", 2000.0, 200.0, 2001, 987654321, 500.0)
checking_acct2 = CheckingAccount("Diana", 1500.0, 100.0, 2002, 987654321, 300.0)

print("\nRunning Scenario...")

print("1. Sarah adds to her savings and earns interest:")
savings_acct1.deposit(200.0)
savings_acct1.apply_interest()

print("\n2. Charlie transfers money to Maddy's savings account:")
checking_acct1.transfer(400.0, savings_acct2)

print("\n3. Charlie attempts a transfer that is too large:")
checking_acct1.transfer(600.0, savings_acct1)

print("\n4. Diana makes a standard withdrawal:")
checking_acct2.withdraw(50.0)