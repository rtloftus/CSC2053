from bank_account import BankAccount

account = BankAccount("00179", 1000)
print(account)

account.deposit(100)
print(account)

account.withdraw(500)
print(account)

account.get_balance()
print(account)