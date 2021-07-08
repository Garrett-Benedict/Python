class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate 
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print (f"balance : {self.balance}")

    def yield_interest(self):
        self.balance += (self.balance*self.int_rate)
        return self

account1 = BankAccount(.01,0)
account2 = BankAccount(.01,0)
account1.deposit(200).deposit(100).deposit(250).yield_interest().withdraw(300).display_account_info()
account2.deposit(500).deposit(30).yield_interest().withdraw(250).withdraw(100).withdraw(200).withdraw(200).display_account_info()