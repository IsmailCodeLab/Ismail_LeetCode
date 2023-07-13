class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        integers=set()
        length=len(nums)
        for i in range(length):
            integer=nums[i]
            rev_integer=0
            tmp=integer
            while tmp>0:
                digit=tmp%10
                rev_integer=rev_integer*10+digit
                tmp//=10
            integers.add(integer)
            integers.add(rev_integer)
            nums.append(rev_integer)
        return len(integers)