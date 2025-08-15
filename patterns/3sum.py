def threeSum(nums):
        n=len(nums)
        nums.sort()
        res=[]
        for i in range(n-1):
            if i>0 and nums[i]==nums[i-1]:
                continue
            else:
                j=i+1
                k=n-1
                while j<k:
                    val=nums[i]+nums[j]+nums[k]
                    if val==0:
                        res.append([nums[i],nums[j],nums[k]])
                        j+=1
                        while nums[j]==nums[j-1] and j<k:
                            j+=1
                    elif val>0:
                        k-=1
                    else:
                        j+=1
        return res
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums)) 