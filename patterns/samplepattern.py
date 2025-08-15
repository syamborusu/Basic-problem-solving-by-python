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

print("_______________________________________________________")
        

def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_val=i
        for j in range(i+1,n):
            if arr[j]<arr[min_val]:
                min_val=j
                arr[i],arr[min_val]=arr[min_val],arr[i]
    return arr
arr=[0,4,2,6,7,1]
print("Before sorting:", arr)
sorted_arr = selection_sort(arr)
print("After sorting:", sorted_arr)

