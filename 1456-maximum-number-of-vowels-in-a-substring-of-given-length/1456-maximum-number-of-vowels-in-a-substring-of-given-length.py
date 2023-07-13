class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=['a','e','i','o','u']
        max_cnt=0
        start=0
        end=0
        cnt=0
        while(end<len(s)):
            if(end<k):
                if s[end] in vowels:
                    cnt+=1
                end+=1
                max_cnt=cnt
            else:
                #temp=s[start:end+1]
                #cnt=sum([temp.count(i) for i in vowels])
                 
                if (s[end] in vowels) and (s[start] not in vowels):
                    cnt+=1
                elif (s[end] not in vowels) and (s[start]  in vowels):
                    cnt-=1
                if max_cnt<cnt:
                    max_cnt=cnt
                start+=1
                end+=1
        if max_cnt>k:
            return k
        else:
            return max_cnt
