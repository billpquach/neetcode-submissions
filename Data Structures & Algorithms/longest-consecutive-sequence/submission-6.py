class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hmap = {...}
        # for i in nums         O(n)
        #   while i+1 in seen   O(n) BUT remove from seen 
        #   
        #   {1,2,3,4,5,6,7}
        #

        seen = set(nums)
        start = set()
        

        for i in seen:
            if i-1 not in seen:
                start.add(i)

        # res = {0, 1}
        if len(seen) == 0:
            return 0
        if len(seen) == 1:
            return 1
        
        sequences = [[] for _ in range(len(start))] 
        #print(sequences)
        j = 0
        for i in range(len(nums)):
            if nums[i] in start:
                #print(j)
                curStart = nums[i]
                start.remove(curStart)
                seen.remove(curStart)
                sequences[j].append(nums[i])
                while curStart+1 in seen:
                    sequences[j].append(curStart+1)
                    curStart += 1
                    seen.remove(curStart)
                j+=1

        maxLen = float("-inf")
        for i in range(len(sequences)):
            maxLen = max(maxLen, len(sequences[i]))
        return maxLen