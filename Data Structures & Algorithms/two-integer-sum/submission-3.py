class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l,r=0,len(nums)-1
        while l<r:
            if nums[l]+nums[r]==target:
                return [l,r]
            if r-1==l:
                l+=1
                r=len(nums)-1
                continue
            
            r-=1