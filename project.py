#Parent class
items_dict = {'1':'Black Shirts' , '2':'Beige trousers' , '3':'Blue Shirt' , '4':'Black trousers'}
class ApparelManager:
	def __init__(self, account_number, account_name, email_id):
		self.account_number = account_number
		self.account_name = account_name
		self.email_id = email_id
	
	def purchase(self, account_number):
		print("Hey! What would you like to purchase?\n\n\
			1. Shirts\n\
			2. Trousers\n")
		
		choice1 = int(input("Enter your option:"))

		if choice1 == 1:
			print("1. Black Shirts\n\
				   3. Blue Shirt\n ") 


		elif choice1 == 2:
			print("2. Beige trousers\n\
			       4. Black trousers\n")


		print("Thank You! You will recieve your order in a day.")	
			

	def rent(self, account_number, delivery_address):
		self.delivery_address=delivery_address
		print("Hey! What would you like to rent?\n\n\
			1. Shirts\n\
			2. Trousers\n")

		choice1 = int(input("Enter your option:"))

		if choice1 == 1:
			print("1. Black Shirts\n\
				   3. Blue Shirt\n ") 


		elif choice1 == 2:
			print("2. Beige trousers\n\
			       4. Black trousers\n")


		print("Thank You! You will recieve your order in a day.")

	def exchange(self, account_number, account_name, delivery_address):
		self.account_number=account_number

		exch=input("Reason for exchange:")
		


	




