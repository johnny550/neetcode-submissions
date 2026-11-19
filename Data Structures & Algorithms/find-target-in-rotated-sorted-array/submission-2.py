class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            divider=(l+r)//2
            if target==nums[divider]:
                return divider

            # left hand side of sorted array
            if nums[l]<=nums[divider]:
                if target>nums[divider] or target<nums[l]:
                    l=divider+1
                else:
                    r=divider-1

            # right hand side of sorted array
            else:
                if  target<nums[divider] or target>nums[r]:
                    r=divider-1
                    continue
                else:
                    l=divider+1
        return -1
