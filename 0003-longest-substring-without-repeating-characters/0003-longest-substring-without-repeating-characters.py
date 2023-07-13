class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique=set()
        right=0
        left=0
        maxlen=0
        for right in range(len(s)):
            if s[right] not in unique:
                unique.add(s[right])
                maxlen=max(right-left+1,maxlen)
            else:
                while s[right] in unique:
                    unique.remove(s[left])
                    left+=1
                unique.add(s[right])
        return maxlen