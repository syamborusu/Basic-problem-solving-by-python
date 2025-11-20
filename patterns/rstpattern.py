n=5
for i in range(n):                #initially i=0
    print()
    for j in range(i,n):            #i to n it prits the statement
        print(' ',end=" ")         #prints spaces up to i to n
    for j in range(i):             
         print('@',end=" ")         #print @ with respect to i value
    for j in range(i+1):            #prints @ with respect to i+1 value
         print('@',end=' ')
    print()