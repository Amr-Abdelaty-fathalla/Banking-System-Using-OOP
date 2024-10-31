# Custom Exception
class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' Created.\nBalance = ${self.balance:0.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' Balance = ${self.balance:0.2f}")

    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit Completed.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:0.2f}")

    # Every time we withdraw money we need to check balance to see if you have enough money to complete transaction
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw Completed.")
            self.getBalance()

        except BalanceException as error:
            print(f"\nWithdraw Interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print('\n*******************\n\nTransfer Beginning... 🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer Completed. ✅\n\n*******************')
        
        except BalanceException as error:
            print(f"\nTransfer Interrupted: ❌ {error}")

class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + amount + (amount * 0.05)
        print("\nDeposit Completed.")
        self.getBalance()

class SavingsAccount(InterestRewardsAccount):
    def __init__(self, initailAmount, acctName):
        super().__init__(initailAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print('\nWithdraw Completed.')
            self.getBalance()

        except BalanceException as error:
            print(f'\nWithdraw Interrupted: {error}')

    def transfer(self, amount, account):
        try:
            print('\n*******************\n\nTransfer Beginning... 🚀')
            self.viableTransaction(amount + self.fee)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer Completed. ✅\n\n*******************')

        except BalanceException as error:
            print(f'\n\nTransfer Interrupted: ❌ {error}')
