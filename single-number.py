def singleNumber(nums):
            for data in set(nums):
                if nums.count(data)<2:
                    return data
