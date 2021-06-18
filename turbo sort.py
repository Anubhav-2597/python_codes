t = int(input("enter number of elements in a list: "))
l1 = []
for i in range(t):
    num = int(input("enter number: "))
    l1.append(num)
l1.sort()

for i in l1:
    print(i)