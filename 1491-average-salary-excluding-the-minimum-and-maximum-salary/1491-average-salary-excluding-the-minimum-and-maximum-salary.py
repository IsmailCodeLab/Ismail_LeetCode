class Solution:
    def average(self, salary: List[int]) -> float:
        if(len(salary)>2):
            total=sum(salary)
            return round((total-max(salary)-min(salary))/(len(salary)-2),5)
        else:
            return 0.00000