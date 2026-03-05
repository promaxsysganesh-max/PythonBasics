# Create a account class with two attributes balance and Acc no. Create methods for debit,credit and printing the balance
class Account:
    
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        print(amount, "rs credited successfully!")

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "rs debited successfully!")
        else:
            print("Insufficient balance")

    def get_balance(self):
        print("Balance:", self.balance)


acc1 = Account("Ganesh", 10000)

acc1.debit(20000)   
acc1.credit(10000)  
acc1.get_balance()