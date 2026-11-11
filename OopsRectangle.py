class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


r1 = rectangle(10, 5)
r2 = rectangle(5, 6)

print("Rectangle 1:")
print("Area:", r1.area())
print("Perimeter:", r1.perimeter())

print("\nRectangle 2:")
print("Area:", r2.area())
print("Perimeter:", r2.perimeter())

if r1.area() > r2.area():
    print("r1 is greater")
elif r2.area() > r1.area():
    print("r2 is greater")
else:
    print("equal")
