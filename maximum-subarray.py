def maxSubArray(nums) -> int:
        if not nums:
            return 0
        curr=maxnum=nums[0]
        for num in nums[1:]:
            curr=max(num,num+curr)
            maxnum=max(curr,maxnum)
        return maxnum

