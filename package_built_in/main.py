import math_os_package.math_operation as math
import math_os_package.os_operations as os

n = int(input("Enter a number: "))

print("Square root:", math.square_root(n))
print("Factorial:", math.factorial(n))

a = int(input("Enter base: "))
b = int(input("Enter exponent: "))

print("Power:", math.power(a, b))

print("\nCurrent directory:", os.current_directory())

print("\nFiles and folders:")
print(os.list_files())

folder = input("\nEnter folder name to create: ")
os.create_folder(folder)

print("Folder created successfully!")
