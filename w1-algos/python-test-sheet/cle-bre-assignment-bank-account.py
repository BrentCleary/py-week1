class BankAccount:
    interest = 0.01

    def __init__(self, account_balance=0):
        self.account_balance = account_balance
        
    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        if(amount>self.account_balance):
            print("Insufficient Funds: Charging a $5 fee")
            self.account_balance -= 5
            return self
        else:
            self.account_balance -= amount
            return self

    def display_account_info(self):
        print(self.account_balance)
        return self

    def yield_interest(self):
        if(self.account_balance>0):
            self.account_balance = self.account_balance + (self.account_balance * self.interest)
            return self
        else:
            print("Insufficent Funds")
            return self

John = BankAccount()
Mary = BankAccount()

John.deposit(100).deposit(200).deposit(300).withdraw(400).yield_interest().display_account_info()
Mary.deposit(100).deposit(200).withdraw(300).withdraw(400).withdraw(500).withdraw(600).yield_interest().display_account_info()

