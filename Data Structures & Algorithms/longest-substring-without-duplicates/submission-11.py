class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s == "":
            return 0

        left = 0
        max_length = 1
        max_set = set()

        for right in range(len(s)):

            ## if s[left] != s[right] => add to max set, max_length +=1, right += 1 
            # (i.e continue loop)
            # pwwkew # we gave 2, should be 3

            while s[right] in max_set:          
                max_set.remove(s[left]) 
                left += 1

            max_set.add(s[right])

            max_length = max(max_length, len(max_set))
        
        return max_length

