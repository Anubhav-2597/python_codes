t = int(input("enter number of test cases: "))

for i in range(t):
    num = int(input("enter number: "))
    k = len(str((num)))
    sum = 0
    for i in range(k):
        if (i == 0 or i == k - 1):
            sum = sum + int(num[i])
        else:
            continue
    print("sum is", sum)