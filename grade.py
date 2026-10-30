mark = int(input("Enter student mark:"))

if mark >= 90 and mark <= 100:
	print("A grade")
elif mark >= 80 and mark < 90:
	print("Grade B")
elif mark >= 60 and mark <= 79:
	print("Grade B")
elif mark >= 30 and mark <= 59:
	print("Grade C")
else:
	print("Failed")	
