class Bank:
	def __init__(self,acc_no,name,acc_type,balance):
		self.acc_no = acc_no
		self.name = name
		self.acc_type = acc_type
		self.balance = balance
	
	def deposit(self,amount):
		self.balance =  self.balance + amount 
		print("Amount deposit succesfully")
	
	def withdrawal(self,amount):
		if amount <= self.balance:
			self.balance = self.balance - amount
			print("Amount withdraw succesfully")
		else:
			print("Insuuffiecient balance")
	
	def display(self):
		print("Account number:",self.acc_no)
		print("Name",self.name)
		print("Account type:",self.acc_type)
		print("Balance:",self.balance)
		

b1 = Bank(101010,"Anzil","Savings",1000000)
b1.display()
b1.deposit(25000)
print("Updated balance:",b1.balance)
			
