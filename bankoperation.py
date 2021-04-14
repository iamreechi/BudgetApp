import datetime
import random 
import time 

database = {}

def init():

	
	print("welcome to Sinzu money")

	
	haveAccount = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))
	
	if(haveAccount ==1):
		login()
	elif(haveAccount == 2):
		register()
	else:
		print("you have selected invalid option")
		init()


def login():
	print("Login to your account")

	accountNumberFromUser = input("What is your account number? \n")
	password = input("What is your password \n")


	for accountNumber,UserDetails in database.items():
		if(accountNumber == accountNumberFromUser):
			if(UserDetails[3] == password):
				bankOperation(UserDetails)


	print("Invalid account or password")

	login()

def register():

	print("******* Register *********")
	email =  input("what is your email address \n")
	first_Name = input("what is your first name \n")
	last_Name = input("what is your last name \n")
	password = input("create a password for yourself \n")
	
	accountNumber = generateAccountNumber()

	database[accountNumber] = [first_Name, last_Name, email, password]

	print("Your account has been created")
	print(datetime.datetime.today())
	print("== ==== ====== ========")
	print("Your account number is: %s" % accountNumber)
	print("Make sure you keep is safe")
	print("== ==== ====== ========")

	login()

def bankOperation(user):

	print("welcome %s %s" % ( user[0], user[1]))

	selectedOption = int(input("What would you like to do? (1) Deposit (2) Withdrawal (3) logout \n"))
	

	if(selectedOption == 1):

		depositOperation()

		

	elif(selectedOption == 2):

		withdrawalOperation()


	elif(selectedOption == 3):

		logout()

	else:
		print("you have selected a wrong number")

		bankOperation(user)


def depositOperation():
	
	userDeposit = int(input("How much would you like to deposit? \n"))
	print('your current balance is %s' % userDeposit)
	selectedOption1 = int(input("What would you like to do? (1) continue transaction (2) end \n"))
	if(selectedOption1	== 1):
		login()
	else:
		logout()



def withdrawalOperation():
	
	userAmount = int(input("How much would you like to withdraw? \n"))
	print("take your cash")
	selectedOption1 = int(input("What would you like to do? (1) continue transaction (2) end \n"))
	if(selectedOption1	== 1):
		login()
	else:
		logout()




def logout():
	exit()



def generateAccountNumber():

	print("Account number generator")
	print("..................")
	time.sleep(2)
	return "01" + str(random.randrange(11111111, 99999999))


init()






