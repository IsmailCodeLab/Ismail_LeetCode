from functools import reduce
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        pro=1
        prod=reduce(lambda a,b:a*b,nums)
        if(prod>0):
            return 1
        elif prod<0:
            return -1
        else:
            return 0