n=5
p=65       #ascii code 0f A-Z(65 TO END OF Z)
for i in range(5):           #i is set to range 0-5
    for j in range(i,n):      #i to n value the loop is ittrate
        print(chr(p),end=" ")     #print p value till the loop terminate
    p+=1                #p value is increment by one
    print()            #goes to new line

