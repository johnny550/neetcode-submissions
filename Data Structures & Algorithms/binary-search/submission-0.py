class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            # print("left:", left, "right:", right)
            # print("nums[left]:", nums[left], "nums[right]:", nums[right])
            # print("target:", target)
            divider=abs((left+right)//2)
            # print("divider:", divider)
            if nums[divider] <target:
                left=divider +1
                continue
            elif nums[divider]>target:
                right=divider -1
                continue
            else:
                return divider
        return -1