class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ## O(m*nlogn) Time - want O(n*m) 
        ## O(m*n) Space - want O(m)

        res = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
                ## This gives a -> 0, b -> 1, ...., z-> 25
                ## Creates an "encoding vector' - representing the canonical form of the string
            res[tuple(count)].append(s)

        return list(res.values())


        
