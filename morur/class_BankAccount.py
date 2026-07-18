class BankAccount():
    def __init__(self, accountname_input, accountnumber_input, accountbalance_input):
        #account balance= موجودی حساب
        self.name=accountname_input
        self.number=accountnumber_input
        self.balance=accountbalance_input

    def deposit(self, increase_balance):
        if increase_balance>0:
            self.balance+=increase_balance
            #self.balance=self.balance+ increase_balance
            print(f"{increase_balance} has been deposited! ")
        else:
            print(f"Error! Deposit amount must be greater than zero.")

    def withdraw (self, decrease_balance):

        if decrease_balance<=0:
            print("Error! withdraw amount must be greater than zero.")
        elif self.balance < decrease_balance:
            print(f"Error!{self.balance} is lees dan {decrease_balance}!")
            
        else:
            self.balance-=decrease_balance
            #self.balance=self.balance- decrease_balance 
            print(f"{decrease_balance} has been withdrawn from {self.name}'s account.")

            
    def show_balance(self):
        print(f"{self.name} with {self.number} account number has {self.balance} balance!")

acc1=BankAccount("Ali", 64923, 500)
acc1.deposit(200)
acc1.show_balance()
acc2=BankAccount("Nasim", 87432, 300)
acc2.deposit(-100)
acc2.show_balance()
acc2.deposit(600)
acc2.show_balance()
acc2.withdraw(500)
acc2.show_balance()
acc2.withdraw(-300)
acc2.show_balance()
