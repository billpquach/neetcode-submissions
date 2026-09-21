class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make keys the per letter count for each word

        hMap = defaultdict(int)
        res = []

        for i in range(len(strs)):

            letterCount = [0] * 26
            for j in range(len(strs[i])):
                letterCount[ord(strs[i][j])-ord('a')] += 1
            if tuple(letterCount) not in hMap:
                hMap[tuple(letterCount)] = [strs[i]]
            else:
                hMap[tuple(letterCount)] += [strs[i]]
        for i in hMap:
            res.append(hMap[i])
        return res
