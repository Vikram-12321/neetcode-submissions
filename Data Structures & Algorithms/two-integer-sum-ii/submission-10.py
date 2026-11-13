class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, k, n = 0, 1, len(numbers) - 1
        out = []

        while i < n: 
            k = 0
            while k <= n:
                if numbers[i] + numbers[k] == target and i != k:
                    if i+1 not in out:
                        out.append(i+1)
                    if k+1 not in out:
                        out.append(k+1)
                k += 1

            i += 1
        return out