num = int(input("enter number: "))

count = 0
while(num!=0):
    if num//100 != 0:
        count = count + num // 100
        num = num % 100
    elif num // 50 != 0:
        count = count + num // 50
        num = num % 50
    elif num // 10 != 0:
        count = count + num // 10
        num = num % 10
    elif num // 5 != 0:
        count = count + num // 5
        num = num % 5
    elif num //2 != 0:
        count = count + num // 2
        num = num % 2
    else:
        count = count + 1
        num = 0
print("value of count is: ",count)


