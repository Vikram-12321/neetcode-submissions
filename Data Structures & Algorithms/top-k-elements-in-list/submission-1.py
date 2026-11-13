class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        count = {} # Stores the number of times each element appers in the list

        for num in nums:
            count[num] = 1 + count.get(num, 0) # get(key, default_value)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num)) # push(# of times num appears, num)
            if len(heap) > k:
                heapq.heappop(heap) # for k=1, we remove the smallest element, 
                # which only leaves us (continuisly) with the largest element (since min heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        '''

        ## Better Soln

        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, cnt in count.items():
            freq[cnt].append(num) # freq[1] = all the items that appear 1 time in nums

        res = []
        for i in range(len(freq) - 1, 0, -1): 
            # This example starts at len(freq)-1 stops before 0 and decrements by 1
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res




            