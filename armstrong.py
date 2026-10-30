num = int(input("Enter the num:"))


temp = num
power = 0

while temp > 0:
	power+= 1
	temp //= 10

temp = num
total_sum = 0

while temp > 0:
	digit = temp % 10
	total_sum += digit ** power
	temp //= 10

if total_sum == num:
	print(f"{num} is armstrong number")
else:
	print("Not an armstrong number")
