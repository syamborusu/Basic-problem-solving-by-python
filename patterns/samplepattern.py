n=7
p=65
for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i+1):
        print(chr(p),end=' ')
        p+=1
        if p>90:
            break
    print()
    