#WAP to find square root a series of numbers input by user

t = int(input("enter test cases: "))

for i in range(t):
    num = int(input("enter number: "))
    sqrt = round(num ** 0.5)
    print("square root is",sqrt)

