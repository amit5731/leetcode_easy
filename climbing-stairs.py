def climbStairs(n) -> int:
        pre=1
        curr=1
        while n>0:
            pre,curr=curr,pre+curr
            n=n-1
        return pre
