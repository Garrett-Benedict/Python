class Bank_Account:
    def __init__(self , amount , withdrawal , deposit , times_with , times_dep):
        self.amount = amount
        self.withdrawal = withdrawal
        self.deposit = deposit
        self.times_with = times_with
        self.times_dep = times_dep
    
    def make_withdrawal(self):
        amount = self.amount
        amount -= self.withdrawal
        print(amount)
    
    def make_deposit(self):
        amount = self.amount
        amount += self.deposit
        print(amount)
    
    def add_sub(self):
        amount = self.amount
        amount += self.deposit * self.times_dep
        amount -= self.withdrawal * self.times_with
        print(amount)

person1 = Bank_Account(amount=1000, withdrawal=150 , deposit=175 , times_with=1 , times_dep=3)
person2 = Bank_Account(amount=1000, withdrawal=250 , deposit=200 , times_with=2 , times_dep=2)
person3 = Bank_Account(amount=1000, withdrawal=50 , deposit= 300 , times_with=3 , times_dep=1)

person1.add_sub()
person2.add_sub()
person3.add_sub()