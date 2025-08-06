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
arr=[10,20,30,40,50,60,70,80,90]
target=40
left=0
right=len(arr)-1
print(bs(arr,left,right,target))