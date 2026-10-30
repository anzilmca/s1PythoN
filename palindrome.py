user_input = input("Enter a string or word:")

reversed_input = user_input[::-1]

if(user_input == reversed_input):
	print(f"'{user_input}' is a palindrome")
else:
	print("Not a palindrome")
