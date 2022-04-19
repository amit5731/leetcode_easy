class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s==s[::-1]:
            return s
        first=0
        max_count=0
        temp=""
        while first<len(s):
            for j in range(first,len(s)):
                visited=s[first:j+2]
                if visited==visited[::-1]:
                    if len(visited)>max_count:
                        max_count=len(visited)
                        temp=visited
            first+=1
        print(max_count)
        return temp