def majorityElement(nums]) -> int:
        if len(nums)<2:
            return nums[0]
        app=len(nums)//2
        temp={}
        for data in nums:
            if temp.get(data) and temp[data]>app:
                return data
            temp[data]=temp.get(data,1)+1
