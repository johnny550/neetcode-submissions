class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # list is always in ascending order
        # p1 always < p2
        # p2 alwasy > p1
        # num[p1]+num[p2]=target
        # target-num[p1]=p2 and vice-versa
        p1=0
        p2=len(numbers)-1
        while p1<p2:
            curr_sum = numbers[p1] + numbers[p2]
            if curr_sum == target:
                return [1+p1, 1+p2]
            elif curr_sum < target:
                p1 += 1
            else:
                p2 -= 1
