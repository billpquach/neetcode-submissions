class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we want to count the occurences of each char for str in strs
        res = []
        seen = set()
        hMap = defaultdict(int)

        for i in range(len(strs)):
            curr = [0] * 26
            for j in strs[i]:
                curr[ord(j) - ord('a')] += 1
            if tuple(curr) not in hMap:
                hMap[tuple(curr)] = [strs[i]]
            elif tuple(curr) in hMap:
                hMap[tuple(curr)] += [strs[i]]
    
        for i in hMap:
            res.append(hMap[i])

        return res
        

