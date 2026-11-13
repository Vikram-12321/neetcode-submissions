class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums) - 1
        l, r = 0, n

        out = []

        for j in range(len(nums)):
            # Objective: -nums[j] = nums[i] + nums[k]
            l = j + 1 
            r = n

            target = -nums[j]

            if nums[j] == nums[j-1] and j > 0:
                continue

            while l < r:
                currSum = nums[l] + nums[r]
                
                if currSum > target:
                    r -=1

                elif currSum < target:
                    l +=1

                else:
                    if [nums[j], nums[l], nums[r]] not in out:
                        out.append([nums[j], nums[l], nums[r]])
                    l += 1
                    r -= 1
        return out