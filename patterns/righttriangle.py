
for i in range(5):      #intially i=0,increment by 1 after every inner loop terminate
    for j in range(5-i):        #j=0,upto 5 not include 5 upto 4 only 
        print(" ",end=" ")      #it prints spaces
    for j in range(i+1):         #j=1,increment by 1 with i value incress
        print("#",end=" ")       #prints the statement
    print()
