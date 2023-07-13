class Solution:
    def isValid(self, s: str):
        l=[]
        ch=['[','{','(']
        for i in s:
            if i=='[' or i=='{' or i=='(' :
                l.append(i)
            elif len(l)>0:
                ele=l.pop()
                if ele=='[' and i!=']':
                    return False
                elif ele=='{' and i!='}':
                    return False
                elif ele == '(' and i != ')':
                    return False
            else:
                return False
        if(len(l)==0):
            return True
        else:
            return False        