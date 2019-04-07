from project import ApparelManager

accounts = {}
account_number = 1001
print ("-" *50)
print("Welcome to ABC")

while True:
	print("Hey! What would you like to do today \n\
		1. Create account\n\
		2. Purchase\n\
		3. Rent\n\
		4. Exchange\n\
		5. Exit\n")



	choice = int(input("Enter your option: "))

	if choice == 1:
		account_name = input("Enter account name:")
		email_id = input("Enter email id:")

		accounts[account_number] = ApparelManager(account_name, account_number, email_id)
		print(accounts)

		print(f"Account created successfully! Your account number is {account_number}")

		account_number += 1



	elif choice == 2:
		account_name = input("Enter account name:")
		account_number = int(input("Enter account number:"))
		size = int(input("Enter your size:"))

		delivery_address = input("Enter the delivery address: ")

		purchase1 = accounts[account_number].purchase(account_number)
		print(purchase1)

		
	elif choice == 3:
		account_number = int(input("Enter your account number:"))
		account_name = input("Enter your account name:")
		delivery_address = input("Enter the delivery address:")
		rent1 = accounts[account_number].rent(account_number, delivery_address)
		print(rent1)
		print("Thanks for choosing us!")



	elif choice == 4:
		account_number = int(input("Enter your account number:"))
		account_name = input("Enter your account name:")
		delivery_address = input("Enter the delivery address:")
		exchange1 = accounts[account_number].exchange(account_number, account_name, delivery_address)
		

	else:
		print("Thanks for shopping with us. Have a nice day!!")
		break
		
