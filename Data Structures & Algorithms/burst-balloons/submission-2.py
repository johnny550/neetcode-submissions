class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        # state = remaining indices (re-calculated)

        # to calculate each state, try popping each balloon and make recursive calls

        # 1 balloon -> 1 
        # 2 balloons -> 2 * 1
        # 3 balloons -> 3 * 2 * 1
        # ...

        # time complexity: O(n!)
        # space complexity: ??


        memo = {}       # nums: 
        def get_max_coin(nums: Tuple[int]):
            
            if len(nums) <= 1:
                return sum(nums)
            
            if nums in memo:
                return memo[nums]
            
            max_coins = 0
            for i, num in enumerate(nums):
                coins = num * (nums[i-1] if i-1 >= 0 else 1) * (nums[i+1] if i+1 < len(nums) else 1)
                coins += get_max_coin(nums[:i] + nums[i+1:])
                max_coins = max(max_coins, coins)
            
            memo[nums] = max_coins
            return max_coins
            
        return get_max_coin(tuple(nums))

            
            

        
