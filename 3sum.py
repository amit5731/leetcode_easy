class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return nums
        target=0
        res=[]
        nums=sorted(nums)
        for idx,data in enumerate(nums):
            #print("data is",data)
            remain=-data
            start=idx+1
            end=len(nums)-1
            while start<end:
                if nums[start]+nums[end]==remain and [nums[start],nums[end],nums[idx]] not in res :
                    res.append([nums[start],nums[end],nums[idx]])
                    start+=1
                    end-=1
                elif (nums[end]+nums[start]>remain) :
                    end-=1
                else:
                    start+=1
        return res
                
            
            