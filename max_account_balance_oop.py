#check which account has the most balance

class Bank:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def findMaxBalance(self, account_list):
        if (len(account_list) == 0):
            return None
        else:
            max_balance = max(account_list, key = lambda x: x.balance)
            return max_balance

account_list = []
a = int(input("Enter total number of comparions: "))

for i in range(1,a+1):
    name = input("Name: ")
    account_number = int(input("Account Number: "))
    balance = int(input("Account Balance: "))
    account_list.append(Bank(name, account_number, balance))


obj = Bank(name, account_number, balance)
records = obj.findMaxBalance(account_list)

if records == None:
    print("No Data Found")
else:
    print("")
    print("The account with the highest account balance is:")
    print("Name: ", records.name)
    print("Account Number: ", records.account_number)
    print("Account Balance: ", records.balance)
