t = int(input("enter number of test cases: "))

for i in range(t):
    num = int(input("enter number: "))
    fact = 1
    for i in range(num):
        fact = fact * num
        num -= 1
    print("factorial is: ", fact)

