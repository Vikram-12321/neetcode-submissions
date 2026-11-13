class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, k = 0, len(s) - 1

        while i < k:
            while i < k and not s[i].isalnum():
                i += 1

            while i < k and not s[k].isalnum():
                k -= 1

            if s[i].lower() != s[k].lower():
                return False
                
            i += 1
            k -= 1
        return True