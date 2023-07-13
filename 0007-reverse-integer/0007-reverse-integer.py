class Solution:
    def reverse(self, x: int) -> int:
        num=abs(x)
        if x<0:
            rev=(-1)*int(str(num)[::-1])
        else:
            rev=int(str(num)[::-1])
        if -2**31 <= rev <= 2**31 - 1:
            return rev
        else:
            return 0
