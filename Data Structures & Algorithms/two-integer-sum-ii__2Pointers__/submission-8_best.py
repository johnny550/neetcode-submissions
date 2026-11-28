class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1,p2=0,len(numbers)-1
        while p1<p2:
            if p1>=p2:
                break
            sum_numbers=numbers[p1]+numbers[p2]
            if sum_numbers>target:
                p2-=1
            elif sum_numbers<target:
                p1+=1
            else:
                return[1+p1, 1+p2]
        return []
