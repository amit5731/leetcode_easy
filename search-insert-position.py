 def searchInsert(nums,target) -> int:
        if target in nums:
            return nums.index(target)
        for idx,data in enumerate(nums):
            if data>target:
                return idx
        return idx+1
