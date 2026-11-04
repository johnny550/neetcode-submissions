class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumOfTwo={}
        for i,v in enumerate(nums):
            num_to_check=target-v
            if num_to_check in sumOfTwo:
                part_one=sumOfTwo[num_to_check]
                part_two=i
                # just to verify
                is_true=(nums[part_one]+nums[part_two]==target)
                if is_true:
                    return [part_one, part_two]
            sumOfTwo[v]=i
        print("sumOfTwo ", sumOfTwo)

            