# This function adds two numbers
def add(x, y):
    return x+y
# This function substracts two numbers
def subtract(x, y):
    return x-y
# This function multiplies two numbers
def multiply(x, y):
    return x*y
# This function divides two numbers
def divide(x, y):
    return x/y
num1 = int(input("100 1"))
num2 = int(input("150 2"))

print("Sum:", add(num1, num2))
print("Difference:", subtract(num1, num2))
print("Product:", multiply(num1, num2))
print("Quotient:", divide(num1, num2))