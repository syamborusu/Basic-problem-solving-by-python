#bianry search
def bs(arr,left,right,target):
    while left<=right:
         mid=(left+right)//2
         if arr[mid]==target:
             return mid
         elif arr[mid]<target:
             left=mid+1
         else:
             right=mid-1
    return-1    
arr=[2,3,4,5,6,7,]
target=7
left=0
right=len(arr)-1
print(bs(arr,left,right,target))