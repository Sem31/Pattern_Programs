n=5
k=4
for i in range(0,n):
    for l in range(0,k):
        print(end=" ")
    k = k-1
    for j in range(0,i):
        print(end="*")
    print("")

for i in range(0,5):
    for j in range(0,i):
        print(end="*")
    print(" ")

print("\n")
n = 5
k=0

for i in range(1,n+1):
    for s in range(1,(n-i)+1):
        print(end=" ")
    while k != (2*i-1):
        print("*",end="")
        k = k+1
    k=0
    print("")
