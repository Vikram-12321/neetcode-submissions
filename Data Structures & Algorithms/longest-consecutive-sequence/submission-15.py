class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # if len(nums) == 100000:
        #     return 2 if nums[0] == -100000000 else 100000

        
        nums_set = set(nums)
        longest_streak = 0

        for num in nums:
            if (num-1) not in nums_set:
                length = 0

                while (num + length) in nums_set:
                    length += 1
                
                longest_streak = max(longest_streak, length)
        
        return longest_streak