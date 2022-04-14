def lengthOfLongestSubstring(self, s: str) -> int:
          first=0
          count=0
          if len(s)<2:
              return len(set(s))
          while first<len(s):
              last_visited=s[first]
              for second in range(first+1,len(s)):
                  if s[second] in last_visited:
                      count = max(count, len(last_visited))
                      break
                  elif s[first]==s[second]:
                      temp=s[first:second]
                      count=max(count,len(temp))
                      break
                  last_visited += s[second]
                  count = max(count, len(last_visited))
              first+=1
          return count