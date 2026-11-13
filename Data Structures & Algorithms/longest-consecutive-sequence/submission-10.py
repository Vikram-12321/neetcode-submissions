class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_streak = 0

        for num in nums_set:
            if (num-1) not in nums_set:
                curr_num = num
                curr_streak = 1

                while (curr_num + 1) in nums_set:
                    curr_num += 1
                    curr_streak += 1
                
                longest_streak = max(longest_streak, curr_streak)
        
        return longest_streak