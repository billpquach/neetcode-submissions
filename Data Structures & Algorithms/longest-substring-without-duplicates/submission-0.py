class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # a variable range such that output = (right bound) - (left bound) + 1
        # two pointer/ sliding window problem
        # use hash set for O(1) lookup
        # {} s[r] == 'x'
        # while s[r] in seen:
        #       seen.remove(s[l])
        #       l += 1
        # seen.add(s[r])
        
        # r is constanly incrementing, no condition

        if len(s) <= 1:
            return len(s)

        seen = set()
        # p w w k e w
        # l   r
        # {y, x}
        l = 0
        res = 0
        for r in range(len(s)):
            
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, (r - l + 1))
        return res



