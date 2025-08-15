n=int(input("enter value="))
p=int(input("enter value="))
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=" ")
    p+=1
    print()
p=70
k=n-1
for i in range(k):
    for j in range(k-i):
        print(chr(p),end=' ')
    p+=1
    print()

    

    