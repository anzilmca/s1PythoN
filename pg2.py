list1 = [11,-21,0,45,66,-93]
for num in list1:
	if num>= 0:
		print(num,end = " ")
		
n = int(input("\nEnter limit:"))
squares = [i * i for i in range(n)]
print("squares of n numbers\n",squares)


word  = input("Enter word:")
for letter in word:
	if letter in 'aeiou':
		print(letter,end=" ")
		
		

list2 = ['aravind','aparna']
print("Original List2:\n" + str(list2))
res = [ord(ele) for sub in list2 for ele in sub]
print("The ASCI list is :\n" +str(res))
