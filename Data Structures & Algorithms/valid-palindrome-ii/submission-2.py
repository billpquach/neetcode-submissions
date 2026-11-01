class Solution:
    def validPalindrome(self, s: str) -> bool:
        # NEEDS:
        # basic palindrome checker; left, right two pointer
        #                           if l != r: return False
        # l != r logic change
        #   if shifted == True: return False

        # 
        # a   b   d   d   a     shifted = False -> True
        # l               r check l+1 == r: l += 1; r - 1 == l: r -= 1
        
        # lcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucul
        #  l                                                             r

        # naive check for next element does not work
        # prioritizes l pointer
        l, r = 0, len(s) - 1
        shifted = False
        while l < r:

            print (s[l], s[r])
            if s[l] != s[r]:
                if shifted == True: return False # false if previously deleted

                elif s[l + 1] == s[r] and s[l + 2] == s[r - 1] if r - l >= 2 else True:
                    l += 1
                    shifted = True
                elif s[r - 1] == s[l] and s[r - 2] == s[l + 1] if r - l >= 2 else True:
                    r -= 1
                    shifted = True
                
                else:
                    return False
            
            l += 1
            r -= 1

        return True
