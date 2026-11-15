class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # a dynamic length substring
        # bounded by right index and left index
        # such that length = right index - left index + 1
        # lookup if current element has already been seen in O(1) time
        # hashset

        # seenItems = {y, z}

        # z x y z x y z
        #     l   r

        seenItems = set()
        res = 0
        l = 0
        # right pointer behavior independent
        for r in range(len(s)):
            while s[r] in seenItems:
                seenItems.remove(s[l])
                l += 1
                
            seenItems.add(s[r])
            res = max(res, r - l + 1)
        return res
            
        

        


