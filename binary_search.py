import math


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # divider
        left,right=0,len(nums)-1
        while left<=right:
            print("left:", left, "right:", right)
            print("nums[left]:", nums[left], "nums[right]:", nums[right])
            print("target:", target)
            divider=math.floor((left+right)//2)
            if nums[divider] <target:
                left=divider +1
                # continue
            elif nums[divider]>target:
                right=divider -1
                # continue
            else:
                return nums[divider]

        return -1

            

sol=Solution()
nums=[-1,0,2,4,6,8]
target=3
# nums=[-1,0,3,5,9,12]
# target=9
print(sol.search(nums, target))