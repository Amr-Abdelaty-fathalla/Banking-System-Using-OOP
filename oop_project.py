from bank_accounts import *

Amr = BankAccount(10000, 'Amr')
Ali = BankAccount(7000, 'Ali')

Amr.getBalance()
Ali.getBalance()

Amr.deposit(5000)

Amr.withdraw(13000)
Amr.getBalance()
Amr.withdraw(13000)

Ali.transfer(6000, Amr)

Mohsen = InterestRewardsAccount(4000, 'Mohsen')

Mohsen.getBalance()

Mohsen.deposit(3000)

Mohsen.transfer(1150, Amr)

Mohsen.getBalance()

Amr.getBalance()

Hana = SavingsAccount(9000, 'Hana')

Hana.getBalance()

Hana.deposit(6000)

Hana.withdraw(4000)

Hana.transfer(2000, Amr)

Amr.getBalance()

Hana.getBalance()

Hana.transfer(9290, Amr)