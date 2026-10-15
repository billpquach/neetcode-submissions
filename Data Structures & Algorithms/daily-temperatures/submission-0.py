class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # if we init a monotonic stack
        # s.t. we only allow smaller values
        # and pop all once a larger value shows up
        # the length of the stack is the value of the idx of the
        results = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                results[index] = i - index
            stack.append(i)

        return results
