n = input("Enter a number (n): ")
terms = int(input("How many terms: "))


sequence = [int(n * i) for i in range(1, terms + 1)]

print(f"Sequence: {' + '.join(map(str, sequence))}")
print(f"Total Sum: {sum(sequence)}")

