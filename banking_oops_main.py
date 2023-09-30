class BankAccount:

  def __init__(self, account_number, account_holder):
    self.account_number = account_number
    self.account_holder = account_holder
    self.balance = 0

  def deposit(self, amount):
    self.balance = self.balance + amount
    return self.balance

  def withdraw(self, amount):
    if amount > self.balance:
      print('Insufficient Balance')
    else:
      self.balance = self.balance - amount
      return self.balance

  def get_balance(self):
    return self.balance


class SavingsAccount(BankAccount):

  def __init__(self, account_number, account_holder, interest_rate):
    super().__init__(account_number, account_holder)
    self.interest_rate = interest_rate

  def addInterest(self):
    interest = self.balance * self.interest_rate / 100
    self.balance = self.balance + interest
    return self.balance


class CurrentAccount(BankAccount):

  def __init__(self, account_number, account_holder, overdraft_limit):
    super().__init__(account_number, account_holder)
    self.overdraft_limit = overdraft_limit

  def withdraw(self, amount):
    if amount > self.balance + self.overdraft_limit:
      print("OD Limit exceeded")
    else:
      self.balance = self.balance - amount
    return self.balance


rohan = SavingsAccount('232', "sb", 8)
print(rohan.deposit(1000))
print(rohan.balance)
print(rohan.withdraw(200))
print()

for i in range(5):
  print(f"Balance after {i+1} years is: ", round(rohan.addInterest(), 2))
  i += 1

print("\nFinal Balance is:", rohan.balance)
