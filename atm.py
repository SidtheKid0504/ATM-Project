class ATM:
    def __init__(self, atmPin, atmCardNumber): 
        self.atmPin = atmPin
        self.atmCardNumber = atmCardNumber
        self.balance = 1000
        
    def checkBalance(self):
        print("Balance is " + str(self.balance))
    
    def withdrawMoney(self):
        withdrawAmount = int(input("How much money: $"))
        if withdrawAmount > self.balance:
            print("Do Not Have Enough Money In Bank")
        else:
            self.balance -= withdrawAmount
            print("Remaining Balance: " + str(self.balance))
    
    def depositMoney(self):
        depositAmount = int(input("How much money: $"))
        self.balance += depositAmount

        print("New Balance: " + str(self.balance))


pin = input("Atm Pin Number: ")
cardNum = input("Card Number: ")
atm = ATM(pin, cardNum)

while True:
    action = int(input("What Do You Want To Do(1=Check Balance, 2=Withdraw, 3=Deposit, 4=Exit): "))

    if action == 1:
        atm.checkBalance()
    elif action == 2:
        atm.withdrawMoney()
    elif action == 3:
        atm.depositMoney()
    elif action == 4:
        break
    else:
        print("There is no action")


    