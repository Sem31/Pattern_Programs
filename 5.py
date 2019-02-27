n = int(input("enter the value : "))
k = 0
for i in range(0,n):
   
    for j in range(i,n):
        print(end="*")
    print("")
    for l in range(0,k+1):
        print(end=" ")
    k = k+1
