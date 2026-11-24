class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[i for i in range(2*len(nums))]
        for i,val in enumerate(nums):
            ans[i]=nums[i]
            ans[i+len(nums)]=nums[i]
        return ans