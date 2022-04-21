class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        
        start=0
        end=len(height)-1
        max_distance=0
        while start<end:
            max_distance=max(max_distance,min(height[start],height[end])*(end-start))
            if height[start]>height[end]:
                end=end-1
            else:
                start+=1
        #print(max_distance)
        return max_distance
            