t = int(input("enter the number of test cases: "))

for i in range(t):
    num = input("enter number: ")
    l1=len(num)
    num = int(num)
    l1 = int(l1)
    rev = 0
    for i in range(l1):
        rev = rev*10 + num%10
        num = num//10
    print("the reverse is: ", rev)