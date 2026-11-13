class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        parent = {num: num for num in nums} 
        size = {num: 1 for num in nums}

        def union(x,y): #(parent, parent)
            root_x = find(x)
            root_y = find(y)

            # if size[root_x] > size[root_y]:
            #     parent[root_y] = root_x
            #     size[root_x] += size[root_y]
            # else:
            #     parent[root_x] = root_y
            #     size[root_y] += size[root_x]

            parent[root_x] = root_y
            size[root_y] += size[root_x]

        def find(x): #(child or parent)
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        
        for num in parent:
            if num + 1 in parent:
                union(num, num+1)

        return max(size.values()) if size else 0
        





        
