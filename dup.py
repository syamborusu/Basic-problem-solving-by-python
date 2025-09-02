#remove duplicates from a list
list=[1,2,0,1,5,2,6]
a =set()
for i in list:
    a.add(i)
print("List after removing duplicates:", a)
print("___________________________________________")