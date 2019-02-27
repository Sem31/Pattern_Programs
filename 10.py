n = int(input("enter the no. : "))

for i in range(0,n+1):
    for j in range(0,i):
        print(end = "*")
    print("")

l = n
for i in range(0,n):
    for j in range(0,l):
        print(end= "*")
    l = l-1
    print(" ")
p = n
for i in range(0,n):
    for j in range(0,p):
        print(end=" ")
    p = p-1
    for k in range(0,i):
        print(end="*")
    print(" ")


o = n
for i in range(0,n):
    for k in range(0,o):
        print(end="*")
    for j in range(0,o):
        print(end=" ")
    o = o-1
    print(" ")

