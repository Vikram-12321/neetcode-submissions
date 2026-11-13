class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1]*len(nums)
        left_prod = [1]*len(nums)
        right_prod = [1]*len(nums)
        

        for i, elem in enumerate(nums):
            j = 0
            while j < i:
                left_prod[i] *= nums[j]
                j += 1
            
            k = len(nums) - 1
            while k > i:
                right_prod[i] *= nums[k]
                k -=1

            res[i] = left_prod[i]*right_prod[i]
        
        return res
            

            
        