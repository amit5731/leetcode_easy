 def moveZeroes(nums):
        for idx,data in enumerate(nums):
              if data==0:
                    nums.append(0)
                    nums.remove(0)
        
