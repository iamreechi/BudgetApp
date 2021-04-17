#create a class 
##BudgetClass
#--Depositing funds, Withdrawing fund, Computing category balances, Transferring balance amounts between categories
#  food, clothing, and entertainment.

class Category:
    
    def __init__(self, categName):
        self.ledger = []
        self.balance = 0.0
        self.categoryName = categName

    def deposit(self, amount, description = ""):
        
        
        self.ledger.append({"amount": float(amount), "description": description})
        self.balance = self.balance + float(amount)
        print(self.ledger)
        

    def withdraw(self, amount, description = ""):


        if self.check_funds(amount) == False:
            print("You don't have sufficient fund for this transaction")
        
            exit()
        else:
            
            self.ledger.append({"amount": (0 - float(amount)), "description": description})
            self.balance = self.balance - float(amount)
            print(self.ledger)
            return True
      
 
    def get_balance(self):
        return self.balance

    def transfer(self, amount, categName):
        
        if self.check_funds(float(amount)):
            self.withdraw(float(amount), "Transfer to "+ categName.categoryName)
            categName.deposit(float(amount), "Transfer from " + self.categoryName)
            return True
        return False

    def check_funds(self, amount):
       
        if float(amount) > self.balance:
            return False
        return True



print("*****Food store******")
food = Category("Food")
food.deposit(int(input("How much will you like to deposit?\n")), "initial deposit")
food.withdraw(int(input("How much will you like to withdraw for groceries?\n")), "groceries")

print("Your food balance is........", food.get_balance())



print("*****clothing store******")
clothing = Category("Clothing")
food.transfer(int(input("How much will you like to transfer from food account?\n")), clothing)
print("Your food balance is........",food.get_balance())
clothing.withdraw(int(input("How much will you like to withdraw for clothing?\n")))
print("Your clothing balance is........",clothing.get_balance())


print("******Entertainment*******Burna boy live concert ticket*****")
ent = Category("entertainment")
ent.deposit(int(input("How much will you like to deposit for Burna boy concert?\n")), "initial deposit")
ent.withdraw(int(input("How much will you like to withdraw for ticket?\n")))
print("Your entertainment balance is........",ent.get_balance())