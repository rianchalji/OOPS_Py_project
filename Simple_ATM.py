class ATM:
    def __init__(self,owner,pin,balance=0):
        self.owner=owner
        self.pin=pin
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposit Amount :{amount} \n New Balance:{self.balance}")
    def withdraw(self, amount):
        if amount>self.balance:
            print("Sufficient Balance")
        else:
            self.balance-=amount
            print(f"Withdraw Amount : {amount} \n New Balance :{self.balance}")   
    def AccountBalance(self):
        print(f"Current Balance :{self.balance}")  
    def PinChange(self,old_pin,new_pin):
        if self.pin==old_pin:
            self.pin=new_pin
            print("Pin change Successfully")
        else:
            print("You have entered Wrong Pin")    
account = ATM("Rianchal", 1234)
account.deposit(500)
account.withdraw(200)
account.account_balance()
account.withdraw(400)
account.pin_change(1234, 5678)
account.pin_change(1234, 1111)
