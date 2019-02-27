n =1
for i in range(1,6):
    for j in range(1,i):
        print(n, end=" ")
        n = n+1
    print("")


n=1
k=4
for i in range(0,5):
    for l in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i):
        print(n,end="")
        n = n+1
    print("")


n=1
k=4
for i in range(0,5):
    for l in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i):
        print("*",end=" ")
    print(" ")
