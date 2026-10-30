line = input("Enter text:")
counts = {}
sentance = line.split()

for word in sentance:
	if word in counts:
		counts[word]+=1
	else:
		counts[word]=1
for k,v in counts.items():
	print(k,v)
