start_year = int(input("Enter start year:"));
end_year = int(input("Enter the end year:"))

print("List of leap years")

for year in range(start_year,end_year):
	if((year % 4 == 0) and (year%100 !=0)) or (year % 400 == 0):
		print(year) 
