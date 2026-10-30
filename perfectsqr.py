limit = int(input("Enter the limit: "))

print(f"Perfect squares of even numbers up to {limit}:")

for i in range(1, limit + 1):
    
    sqrt = i ** 0.5
    
    if sqrt.is_integer() and int(sqrt) % 2 == 0:
        print(f"{i} (which is {int(sqrt)})")

