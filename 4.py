n = int(input("enter the value : "))
k = 3
for i in range(0,n):
    for l in range(0,k+1):
        print(end=" ")
    k = k-1
    for j in range(0,i):
        print(end="*")
    print("")
