#bianry search
def bs(arr,left,right,target):
    if target not in arr:
        return -1
    while left<=right:
         mid=(left+right)//2
         if arr[mid]==target:
             return mid
         elif arr[mid]<target:
             left=mid
         else:
             right=mid
    return-1    
arr=[10,20,30,40,50,60,70,80,90]
target=50
left=0
right=len(arr)-1
print(bs(arr,left,right,target))