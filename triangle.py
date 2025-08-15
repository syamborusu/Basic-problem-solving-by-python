n=int(input("value="))
for i in range(n):         #outter loop,row
    print()                 #new line
    for j in range(i+1):    #inner loop,colum
        print("#",end=" ")  #end for same line

print()