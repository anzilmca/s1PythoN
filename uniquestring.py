text = input("Enter string")

unique_str = ""

for char in text:
	if char not in unique_str:
		unique_str += char

print(f"unique characters:{unique_str}")
