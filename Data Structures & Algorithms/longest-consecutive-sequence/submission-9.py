class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        parent = {num: num for num in nums} 
        size = {num: 1 for num in nums}
        max_value = 1 if nums else 0

        def union(x,y): #(parent, parent)
            nonlocal max_value
            root_x = find(x)
            root_y = find(y)
            
            parent[root_x] = root_y
            size[root_y] += size[root_x]

            if max_value < size[root_y]:
                max_value = size[root_y]
            

        def find(x): #(child or parent)
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        
        for num in parent:
            if num + 1 in parent:
                union(num, num+1)

        return max_value
        





        
